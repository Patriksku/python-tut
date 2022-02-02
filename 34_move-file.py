import os

source = "C:\\Users\\fourseven\\Desktop\\test.txt"
destination = "C:\\Users\\fourseven\\Desktop\\wow\\test2.txt"

# Can also be used to move directories.
try:
    if not os.path.exists(source):
        print("File at source does not exist.")
    elif os.path.exists(destination):
        print("There is already a file at destination.")
    else:
        os.replace(source, destination)
        print(source + " was moved to: " + destination)

except FileNotFoundError:
    print(source + " not found.")










