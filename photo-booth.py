# File Renaming Script for Photo Booth files on MacOS
# Originally created: June 30th, 2022
# By Mufasa A. | mufasa159

import os

print("-------------------------------------------- How To Guide -----")
print(" 1. Never use quotation marks (\"\") \n 2. Type 'end' anytime to exit")
print("---------------------------------------------------------------\n")

files = ""
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

if path[-1] != "/":
    path = path + "/"

for j in files:
    old_name = path + j
    name = j.lower()
    if name[0:5] == "movie" or name[0:5] == "photo":
        temp = name.split()

        # get date and time from filename
        date = temp[2].split("-")
        time = temp[4].split(".")

        # format year
        year = "20" + date[2]

        # format month
        if len(date[0]) == 1:
            month = "0" + date[0]
        else:
            month = date[0]

        # format day
        if len(date[1]) == 1:
            day = "0" + date[1]
        else:
            day = date[1]

        # format hour
        if temp[5][:2] == "am":
            if len(time[0]) != 1:
                hour = time[0]
            else:
                hour = "0" + time[0]
        else:
            hour = str(int(time[0]) + 12)
            if len(hour) != 1:
                hour = hour
            else:
                hour = "0" + hour

        # determine file extension
        extension = ""
        if temp[5][-3:] == "mov":
            extension = ".mov"
        elif temp[5][-3:] == "jpg":
            extension = ".jpg"

        # keep track of versions or files made within a minute
        # because they have the same name
        version = ""
        if len(temp) > 6:
            if temp[6][0] == "#":
                version = "_" + temp[6][1]

            if temp[6][-3:] == "mov":
                extension = version + ".mov"
            elif temp[6][-3:] == "jpg":
                extension = version + ".jpg"

        new_name = path + year + month + day + "_" + hour + time[1] + extension
        print(new_name)

        # rename all files in the directory
        os.rename(old_name, new_name)
