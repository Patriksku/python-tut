# Higher Order Function =   a function that either:
#                           1. accepts a function as an argument
#                           or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


# Example 1
def hello(func):
    text = func("Hello?")
    print(text)


hello(loud)
hello(quiet)


# Example 2
# x will be 2, and we are returning the function "dividend", and assigning it to the variable "divide"
# we can call a variable, if it has the memory address of a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))
# print(divide)








