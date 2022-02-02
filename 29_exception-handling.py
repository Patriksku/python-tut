# Exception =   events detected during execution that interrupt the flow of a program.

# Method 1 (bad)
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# except Exception:
#     print("Something went wrong...")


# Method 2 (better)
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero.")
except ValueError as e:
    print(e)
    print("Only use numbers please.")
except Exception as e:
    print(e)
    print("Something went wrong... wtf")

# This will execute only of no exceptions occurred.
else:
    print(result)
finally:
    print("This will always execute.")









