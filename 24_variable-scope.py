# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created.
#         LEGB rule -> Local, Enclosing, Global, Built-in   // Priority

name = "Skuz"  # Global version


def display_name():
    name = "Patrik"  # Local version
    print(name)


display_name()
print(name)
