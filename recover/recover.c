#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)      //checking if we see 2 arguments input
    {
        printf("Usage: ./reecover infile\n");
        return 1;
    }

    char *input_file = argv[1];

    //size of buffer
    const int BLOCK_SIZE = 512;

    //opening a file
    FILE *input_r = fopen(input_file, "r");

    //check if it's valid or not
    if (input_r == NULL)
    {
        printf("Could not open file\n");
        return 2;
    }

    unsigned char buffer[BLOCK_SIZE];

    //File pointer for recovered images
    FILE *output_file = NULL;

    // make space for jpg file nam,e
    char image[7];

    //track numbers of images generating
    int count_image = 0;


    //READING 512 BYTES BLOCKS IN BUFFER
    while (fread(buffer, BLOCK_SIZE, 1, input_r) == 1)
    {
        //looking for the header of jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] >= 0xe0 && buffer[3] <= 0xef)
        {
            //close file if one has bee created
            if (count_image > 0)
            {
                fclose(output_file);
            }

            //creating a file name
            sprintf(image, "%03i.jpg", count_image);

            //opening a file
            output_file = fopen(image, "w");

            if (output_file == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", image);
                return 3;
            }


            count_image++;
        }

        //checking for valid input
        if (output_file != NULL)
        {
            //write image file
            fwrite(buffer, BLOCK_SIZE, 1, output_file);
        }
    }

    //closing files and freeing the memory
    fclose(input_r);
    fclose(output_file);

    return 0;
}