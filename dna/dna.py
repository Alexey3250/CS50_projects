import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py databases/small.csv sequences/1.txt ")

    # Read database file into a variable
    with open(sys.argv[1], 'r') as database:
        database_dict = csv.DictReader(database)

        header = database.readline()  # read only first line; returns string
        subseq = header.split(',')  # returns list

        # data cleaning
        subseq[-1] = subseq[-1].strip()  # removing new line character

    # Read DNA sequence file into a variable
    input_txt = open(sys.argv[2], 'r')
    DNA_sequence = input_txt.read()

    # Find longest match of each STR in DNA sequence
    i = 1
    STR_counts = ["?"]  # adding "?" instead of the "name" as a a1st item

    while i < len(subseq):
        STR_counts.append(longest_match(DNA_sequence, subseq[i]))
        i = i + 1

    # Checking database for matching profiles
    with open(sys.argv[1], newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    # declaring variables for loops
    r = 1  # row number avoiding headers at row 0
    row_list = []  # row list array
    match = False

    # iterating through rows of the csv dataset
    while r < len(data) and match == False:
        row_list = data[r]

        i = 1  # row item avoiding 'name' at row_item 0
        counter = 0  # matches counter
        while i < len(row_list) and match == False:
            # counting matches
            if int(row_list[i]) == STR_counts[i]:
                counter = counter + 1
            else:
                counter = 0  # resetting the counter
            # printing the name if all numbers match
            if counter == len(row_list) - 1:
                print(row_list[0])
                match = True
                break

            i = i + 1  # next item in the row
        r = r + 1  # next row

    # we tried everything
    if match == False:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
