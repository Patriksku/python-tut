# *************************************
# if __name__ == '__main__'
# *************************************
#
# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules
#
# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__

# run "module_two.py".
# print(__name__)


def hello():
    print("Hello")


# if __name__ == '__main__':
#     print("running this module directly")
# else:
#     print("running other module indirectly")

if __name__ == '__main__':
    hello()


