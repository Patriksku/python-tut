# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of positional arguments


def add(*args):
    sum = 0

    #  We can cast the args-tuple to a list, so that we are able to change the values.
    args = list(args)
    args[0] = 0
    #

    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5))






