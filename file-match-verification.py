# File Match Verification Script
# Originally created on Mar 14th, 2021
# By Mufasa A. | mufasa159

import os

# string manipulation for cleaning data
def data_clean(original_file, new_file):

    # overwrites (clears) new_file if it already exists
    open(new_file, "w").close()

    with open(original_file) as f:
        lines = f.readlines()

        filter_chars = ["*", ".", "½", "¾", "⅔", "x2", "x3", "x4", "(", ")", "/", "\\"]
        filter_emojis = ['😂', '🤣', '✅', '😁', '😢', '😁', '👍🏽', '👍🏼', '❤️', '🥺', '😄', '🥲', '🙁', '💛', '🧠', '💪', '😭', '😭', '🎥', '🎵', '🙂', '😥', '☺']

        for i in range(0, len(lines)):
            each_line = str(lines[i])

            # gets rid of reviews and watch time
            for char in filter_chars:
                if char in each_line:
                    each_line = each_line.replace(char, "")

            # gets rid of emojis
            for emoji in filter_emojis:
                if emoji in each_line:
                    each_line = each_line.replace(emoji, "")

            # gets rid of list numbers
            each_word = each_line.split()
            each_word[0] = ""
            each_line = (" ".join(each_word)).lstrip()

            # print(each_line)

            # updates new file with clean data
            with open(new_file, "a") as updated_file:
                updated_file.writelines(each_line + "\n")

        print("\nTotal Lines in Original File: " + str(len(lines)))


def file_verify(file, directory):

    if not os.listdir(directory):
        print("No files found in the directory. /n Please select a directory that contains files.")
    else:
        directory_files = os.listdir(directory)
        with open(file) as check_list:
            lines = check_list.readlines()

            for i in range(0, len(lines)):
                each_line = str(lines[i])

                if each_line in directory_files:
                    print(each_line)


# data_clean('movies.txt', "checkList.txt")
file_verify("checkList.txt", "/movies")
