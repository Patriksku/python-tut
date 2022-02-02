path = "C:\\Users\\fourseven\\Desktop\\test.txt"

# Reads file row by row
try:
    with open(path) as file:
        print(file.read())  # Closes automatically after reading.
    print(file.closed)

except FileNotFoundError:
    print("File not found.")






