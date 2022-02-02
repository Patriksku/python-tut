import os

path = "C:\\Users\\fourseven\\Desktop\\test.txt"  # Escape the backslash in a string

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("File = True")
    elif os.path.isdir(path):
        print("Directory = True")
else:
    print("That location does not exist.")














