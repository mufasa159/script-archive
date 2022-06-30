# File Renaming Script
# Originally created: October 8th, 2021
# By Mufasa A. | mufasa159

import os

print("------------------------------------------------------ How To Guide ----")
print(" 1. Never use quotation marks (\"\") \n 2. Enter directory and end with slash (/) \n    i.e. /Users/muhfasulalam/Downloads/\n 3. Type 'y' or 'Y' without quotation mark\n 4. Type 'end' anytime to exit")
print("------------------------------------------------------------------------\n")

path = str(input("Enter directory path: "))

if path == "end" or path == "q" or path == "quit":
    print("Terminating program...")
    os._exit(0)
else:
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print("File not found. Please try again.")
        path = str(input("Enter directory path: "))



def reformat(file_name):
    filter_chars = [',', '_', '?', '/', ';', '-']
    file_types = [".mp4", ".jpg", ".png"]

    name = file_name.lower()
    for char in name:
        if char in filter_chars:
            name = name.replace(char, " ")
        if char == '\'' or char == '?':
            name = name.replace(char, "")

    words = name.split()
    formatted_name = words[0]

    for i in range(1, len(words)):
        if words[i] in file_types:
            y = words[i]
        else:
            y = "-" + words[i]

        formatted_name += y

    return formatted_name



confirmation = str(input("Are you sure you want to rename all files? "))

if confirmation.lower() == "y":
    for j in files:
        old_name = path + j
        new_name = path + reformat(j)
        os.rename(old_name, new_name)
    print("All files renamed successfully!")
elif confirmation.lower() == "end" or confirmation.lower() == "q" or confirmation.lower() == "quit":
    print("Terminating program...")
    os._exit(0)
else:
    print("No files changed")

