import cs50

# get amount of cents
while True:
    cents = cs50.get_float("Change owed: ") * 100
    if cents > 0:
        break

# calculate /25
quarters = cents // 25
cents = cents - quarters * 25
# print(f"Quarters: {quarters}")

# calculate /10
dimes = cents // 10
cents = cents - dimes * 10

# calculate nickels /5
nickels = cents // 5
cents = cents - nickels * 5

# calculate pennies /1
penis = cents

# sum of all coins
coins = int(penis + nickels + dimes + quarters)

# print the amount of coins we are giving back
print(f"{coins}")