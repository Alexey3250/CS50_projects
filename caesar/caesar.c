#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{

    //check if the user has put a single value
    if (argc != 2)
    {
        printf("cannot be cyphered, put only 1 number -_-\n");
        return 1; // return of 1 tends to signify an error
    }


    //If any of the characters of the command-line argument is not a decimal digit,
    // your program should print the message Usage: ./caesar key and return from main a value of 1.


    string s = argv[1]; //converts imput value to a string
    int n = strlen(s); //declaration and measurement of the length of the key

    //printf("argv[1]=%s\n", s); //debug
    //printf("length of the value is n=%i\n", n); //debug

    //lets now check if all the values are digits using isdigit, declared in ctype.h, one digit at a time
    int sum = 0;
    for (int i = 0; i <= n; i++)
    {
        bool d = isdigit(s[i]); //assings 1 if digit, 0 if not
        sum = sum + d;

        //printf("%i\n", d); //debug prinf checking the values

    }

    //printf("sum = %i, length = %i\n", sum, n); //debug line to check the values

    if (sum != n) //checks if the sum of digits equals to the sum of charachters in the key imput.
    {
        printf("Usage: ./caesar key\n");
        return 1; // return of 1 tends to signify an error
    }


    int key = atoi(argv[1]); //converting the string to an integer

    //prompt the user for the text
    string text = get_string("Enter your text: ");

    //afor loop rotating letter by letter
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]))
        {
            //first we need to convert the upper letter to the index of the actual alphabet
            text[i] = text[i] - 65; //A in ASCII is on 65th place
            text[i] = (text[i] + key) % 26; //using the furmula
            text[i] = text[i] + 65; // reverting the i back to ASCII place
        }
        else if (islower(text[i]))
        {
            text[i] = text[i] - 97; //a in ASCII is on 97th place
            text[i] = (text[i] + key) % 26; //using the furmula
            text[i] = text[i] + 97; // reverting the i back to ASCII place
        }
    }
    printf("Ciphertext: %s\n", text);

}

