def hello():
    print("Hello")


print(hello)  # Displays the memory address of this function
hi = hello
print(hi)

hello()
hi()


# say = print
# print(say)

say = print
say("Hey!")



