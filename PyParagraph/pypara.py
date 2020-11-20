#Import dependencies
import os
import re

#set file path for both file options, give user a choice
file = os.path.join("raw_data","paragraph_1.txt")
file2 = os.path.join("raw_data","paragraph_2.txt")
choice = int(input("Which paragraph would you like to analyze? [1] or [2]"))

#Conditional to choose the correct file
if choice == 1:
    with open(file, 'r') as text:
        #read in text file
        paragraph = text.read()
        #split paragraph on punctuation to get sentences
        sentences = re.split("(?<=[.!?]) +", paragraph)
        #split on non-word characters to get word list
        words = re.split(r"\W+", str(sentences))
        #split words into characters to get letter count
        letters = list(str(words))
#same as above but with file 2
elif choice == 2:
    with open(file2, 'r') as text:
        paragraph = text.read()
        sentences = re.split("(?<=[.!?]) +", paragraph)
        words = re.split(r"\W+", str(sentences))
        letters = list(str(words))
#offer up a choice if they do not choose 1 or 2. 
else:
    int(input('Sorry, you entered the wrong value - please try again and enter either "1" or "2"'))

#variables to store output
let_avg = len(letters)/len(words)
sent_count = len(sentences)
word_count = len(words)
sen_len = len(words)/len(sentences)

#print output to terminal
print(f'Paragraph Analysis')
print(f'-----------------')
print(f'Approximate Word Count: {word_count:.1f}')
print(f'Approximate Sentence Count: {sent_count:.1f}')
print(f'Average Letter Count: {let_avg:.1f}')
print(f'Average Sentence Length: {sen_len:.1f}')

output = os.path.join("output","paragraph.txt")
with open(output, 'w', newline="") as writer:
    writer.write(f'Paragraph Analysis\n')
    writer.write(f'----------------------------\n')
    writer.write(f'Approximate Word Count: {word_count:.1f}\n')
    writer.write(f'Approximate Sentence Count: {sent_count:.1f}\n')
    writer.write(f'Average Letter Count: {let_avg:.1f}\n')
    writer.write(f'Average Sentence Length: {sen_len:.1f}\n')