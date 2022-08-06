import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":

        # Query from database an array of current stocks
        user_id = session["user_id"]
        transactions_db = db.execute(
            "SELECT symbol, name, SUM(shares) AS shares, price, total FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
        cash_db = db.execute("SELECT cash FROM users where id = ?", user_id)
        cash = cash_db[0]["cash"]

        # Whole holdings value
        stocks_value_db = db.execute("SELECT SUM(total) FROM transactions WHERE user_id = ?", user_id)
        # return jsonify(stocks_value_db[0]["SUM(total)"])
        if not stocks_value_db[0]["SUM(total)"]:
            stocks_value = cash
        else:
            stocks_value = stocks_value_db[0]["SUM(total)"] + cash

        return render_template("index.html", database=transactions_db, cash=usd(cash), stocks_value=usd(stocks_value))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        shares_check = request.form.get("shares")

        # Check for currect input
        if not symbol:
            return apology("Input the symbol")
        if not shares:
            return apology("Choose number of shares")
        if lookup(symbol) == None:
            return apology("Could not find")
        if not shares_check:
            return apology("Please enter a number of shares.")
        if int(shares_check) < 1:
            return apology("Invalid number of shares.")
        if isinstance(shares_check, int):
            return apology("Invalid number of shares.")

        stock = lookup(symbol.upper())

        # Check if the user has enough money to buy
        transaction_value = shares * stock["price"]
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]

        if user_cash < transaction_value:
            return apology("Sorry, you are too poor")
        else:
            cash_left = user_cash - transaction_value
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_left, user_id)

            # Add the transaction to the transactions table
            id_db = db.execute("SELECT MAX(id) FROM transactions")
            id = id_db[0]["MAX(id)"] + 1
            date = datetime.datetime.now()
            name = stock["name"]
            # return jsonify(stock)
            db.execute("INSERT INTO transactions(id, user_id, symbol, shares, price, date, transaction_type, name, total) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    id, user_id, symbol, shares, stock["price"], date, "buy", name, transaction_value)

            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        user_id = session["user_id"]
        database = db.execute("SELECT symbol, shares, price, date FROM transactions WHERE user_id = ?", user_id)
        return render_template("history.html", database=database)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")

        # Check for currect input
        if not symbol:
            return apology("Input the symbol")

        else:
            if lookup(symbol) != None:
                stock = lookup(symbol.upper())
                return render_template("quoted.html", name=stock["name"], price=usd(stock["price"]), symbol=stock["symbol"])

            else:
                return apology("Could not find")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    else:
        # if POST, get the input
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Checks for correct input
        if not username:
            return apology("Username is blank")

        if not password:
            return apology("Where is your password?")

        if password != confirmation:
            return apology("Passwords do not match")

        # Generating secure hash password
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # If everything is fine, check and store the password
        try:
            if check_password_hash(hash, password):
                # insert into database /line 26
                new_user = db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hash)
            else:
                return apology("Passwords is not secure")
        except:
            return apology("Username already exists")

        # Create a new session
        session["user_id"] = new_user

        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":

        # Query from database an array of current stocks
        user_id = session["user_id"]
        symbols_user = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = :id GROUP BY symbol HAVING SUM(shares) > 0", id=user_id)
        return render_template("sell.html", symbols=[row["symbol"] for row in symbols_user])
    else:
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = -int(request.form.get("shares"))

        # Check for currect input
        if not symbol:
            return apology("Input the symbol")
        if not shares:
            return apology("Choose number of shares")
        if lookup(symbol) == None:
            return apology("Could not find")
        # if not shares.isdigit():
            # return apology("You cannot sell partial shares.")
        # if shares => 0:
            # return apology("You cannot sell negative shares.")

        stock = lookup(symbol.upper())
        transaction_value = shares * stock["price"]

        # Check if the user has enough shares to sell
        portfolio_db = db.execute(
            "SELECT shares FROM transactions WHERE user_id = :id AND symbol =:symbol GROUP BY symbol", id=user_id, symbol=symbol)
        portfolio = portfolio_db[0]["shares"]
        # return jsonify(shares)
        if -shares > portfolio:
            return apology("You don't have enough shares")

        # Add the transaction to the transactions table
        id_db = db.execute("SELECT MAX(id) FROM transactions")
        id = id_db[0]["MAX(id)"] + 1
        date = datetime.datetime.now()
        name = stock["name"]

        db.execute("INSERT INTO transactions(id, user_id, symbol, shares, price, date, transaction_type, name, total) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                id, user_id, symbol, shares, stock["price"], date, "sell", name, transaction_value)

        # Make a money deduction from total cash
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_cash_db[0]["cash"]
        cash_left = user_cash - transaction_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_left, user_id)

        return redirect("/")

