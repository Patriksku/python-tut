def hello(first_name, last_name, age):
    print("Hello " + first_name + ' ' + last_name + '!')
    print("Your age: " + str(age))


# variable number of non keyword arguments passed
def sum_of_numbers(*numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number

    print(total_sum)


name = "Yohari"

hello(name, "Jones", 55)
sum_of_numbers(10, 40, 550)
