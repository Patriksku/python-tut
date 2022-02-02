path = "C:\\Users\\fourseven\\Desktop\\testt.txt"
text = "Yoooo\nthis a text ha.\n"

# Will write to file if it exists, or create a new one @ path.
# 'w' overwrites. 'a' appends.
with open(path, 'a') as file:
    file.write(text)  # Closes automatically after reading.
print(file.closed)



















