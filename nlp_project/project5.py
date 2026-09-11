from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

File_path = os.getenv("File_path")
with open(File_path, "r") as file:
    text = file.read()

user_input = input("Enter your sentence: ")
text = text + " " + user_input

words = text.split()

paragraph = []

for i in range(len(words) - 2):

    current_word = words[i]
    next_word = words[i + 1]
    last_word = words[i + 2]

    sequence = [current_word, next_word, last_word]
    paragraph.append(sequence)
    print("Sequences:")
    for sequence in paragraph:
        print(" ".join(sequence))
