// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//declare variables
unsigned int word_count;
unsigned int hash_value;

// Returns true if word is in dictionary, else falsef
bool check(const char *word)
{
    // TODO
    //hash the word to obtain a hash value
    hash_value = hash(word);
    node *cursor = table[hash_value];

    //go through linked list
    while (cursor != 0)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long total = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        total += tolower(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");

    //if it does not open
    if (file == NULL)
    {
        printf("Unable to open %s\n", dictionary);
        return false;
    }
    //declare varialble called word
    char word[LENGTH + 1];

    //scan dictionary for strings until EOF
    while (fscanf(file, "%s", word) != EOF)
    {
        //accolate memory for new node
        node *n = malloc(sizeof(node));

        //if malloc returns NULL, return false
        if (n == NULL)
        {
            return false;
        }

        //copy word into node
        strcpy(n->word, word);
        hash_value = hash(word);
        n->next = table[hash_value];
        table[hash_value] = n;
        word_count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Iterate through buckets
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor)
        {
            node *tmp = cursor;
            cursor = cursor ->next;
            free(tmp);
        }
        if (cursor == NULL)
        {
            return true;
        }
    }
    return false;
}
