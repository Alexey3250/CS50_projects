#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //declaration of typed in value
    int h;
    // a loop that will prompt you infinitely if 1<=h<=8 is false
    do
    {
        h = get_int("Positive number: ");
    }
    // opposite to 1<=h<=8
    // so it will keep prompting until you type in from 1 to 8
    while (h < 1 || h > 8);
    //printf("Positive number received, h= %d \n", h);


// for loop for rows
    for (int x = 0; x < h; x++)
    {
        //for loop for spaces with n number decreasing each row
        for (int n = h ; n > x + 1; n--)
        {
            printf(" ");
        }

        //for loop for # symbols with # increasing each row
        for (int n = 0; n < x + 1; n++)
        {
            printf("#");
        }
        //breaks the line to another
        printf("\n");
    }

}

