import cs50
import re

# get text
text = cs50.get_string("Text: ")

# count letters
letters = 0
for i in text:
    if(i.isalpha()):
        letters += 1

# count words
words = 0
word_list = text.split()
words = len(word_list)

# count sentences
sentences = len(re.split(r'[.!?]+', text)) - 1

# calculating the index

# L = average number of letters per 100 words in the text
L = (letters / words) * 100

# S = average number of sentences per 100 words in the text
S = (sentences / words) * 100

Coleman_Liau_index = round(0.0588 * L - 0.296 * S - 15.8)

# printing the results
if Coleman_Liau_index < 1:
    print("Before Grade 1")
elif Coleman_Liau_index > 16:
    print("Grade 16+")
else:
    print(f"Grade {Coleman_Liau_index}")

# debug
#print("Letters: ", letters)
#print("words: ", words)
#print("sentences: ", sentences)
#print("L: ", L)
#print("S: ", S)
#print("Coleman_Liau_index: ", Coleman_Liau_index)