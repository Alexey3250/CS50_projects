#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);


// q -25c, d -10c, n-5c, p -1c

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    //the function prompts the user for a number of cents
    //using get_int and then returns that number as an int.
    //If the user inputs a negative int, it prompts user again.
    //e.g., a string, as get_int takes care of the integer
    //and the condition > 0 takes care of the positive imput

    //loop to check for a proper imput
    int change;
    do
    {
        change = get_int("Change owed: "); //gets the value of change owed
    }
    while (change < 0); //positive number condition

    //printf("%d\n", change); //checks the value imput

    return change; //assignes the change amount of cents to the function get_cents
}

int calculate_quarters(int cents)
{
    //нужно посчитать сколько целых 25-ти центовых монет в общем количестве
    //the function calculates (and returns as an int) how many quarters
    //a customer should be given if they’re owed some number of cents.
    //For instance, if cents is 25, then calculate_quarters should return 1.
    //If cents is 26 or 49 (or anything in between, then calculate_quarters should also return 1.
    //If cents is 50 or 74 (or anything in between), then calculate_quarters should return 2. And so forth.
    //pseudocode quarters = Change/25 that's it, the rest is calculated in the upper stage
    return cents = cents / 25;
}

int calculate_dimes(int cents)
{
    // TODO
    return cents = cents / 10;
}

int calculate_nickels(int cents)
{
    // TODO
    return cents = cents / 5;
}

int calculate_pennies(int cents)
{
    // TODO
    return cents = cents / 1;
}
