#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    /**
    imput text
    calculate the letters ( excluding space) - loop
    count spaces to count words - loop
        - spaces count +1 = word count
    count sentences by counting . ! ? - loop
    calculate the Coleman-Lyau index
        index = 0.0588 * L - 0.296 * S - 15.8
        output: rounded up whole number
    **/

    string text = get_string("Text: ");

    //calculating L
    int letters = 0; //total letters

    for (int i = 0; i < strlen(text); i++) // counting letters propely
    {
        if (isalpha(text[i])) //checking for letters
        {
            letters++;
        }
    }

    int spaces = 0; //spaces count
    int sentences = 0; // total sencences

    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i])) //checking for spaces
        {
            spaces++;
        }
        else if (text[i] == 46) //checking for .
        {
            sentences++;
        }
        else if (text[i] == 33) //checking for !
        {
            sentences++;
        }
        else if (text[i] == 63) //checking for ?
        {
            sentences++;
        }
    }
    
    int words = spaces + 1; // counting the words

    float L = (float) letters / words * 100; //l index
    float S = (float) sentences / words * 100; //S index

    //printf("letters:%i words:%i sentences=%i\n", letters, words, sentences);

    int index = (float) round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}