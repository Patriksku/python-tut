# str.format() =    optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item))  # positional arguments
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword arguments

text = "The {} jumped over the {}"
print(text.format(animal, item))


# name = "Bro"
# print("My name {}".format(name))
# print("My name {:10}. Nice to meet you.".format(name))  # Amount of padding (10)
# print("My name {0:10}. Nice to meet you.".format(name))  # Same but with positional argument as an example
# print("My name {:<10}. Nice to meet you.".format(name))  # Standard left align
# print("My name {:>10}. Nice to meet you.".format(name))  # Right align
# print("My name {:^10}. Nice to meet you.".format(name))  # Center align


pi = 3.14159
number = 1000
print("The number pi is {:.2f}".format(pi))  # Two-decimal formatting (also rounds the number)
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))  # In binary
print("The number is {:X}".format(number))  # Hexadecimals
print("The number is {:E}".format(number))  # Scientific notation



