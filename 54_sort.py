# sort() method =   used with lists
# sort() function = used with iterables

# List sorting
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
students.sort()

for i in students:
    print(i)

print()
students.sort(reverse=True)

for i in students:
    print(i)

# Tuple sorting
print()
students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
sorted_students = sorted(students)  # Returns a list

for i in sorted_students:
    print(i)
print()

# List of tuples sorting, based on columns
s_tudents = [("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr. Krabs", "C", 78), ]

# Default sort will sort by the first (0) column, which in this case is the student names.
s_tudents.sort()

for i in s_tudents:
    print(i)
print()

# Let's sort by the second (1) column instead.

# Explanation:
# The lambda creates an inline function for the key parameter.
# Using a lambda would be no different from doing

# def func(x):
#   return x[1]
#
# and then

# lst.sort(key=func)
#
# ----------------------------------------------
# The optional key parameter to sort/sorted is a function.
# The function is called for each item and the return values determine the ordering of the sort
# // print(s_tudents[0][1])
# ----------------------------------------------
grade = lambda x: x[1]
s_tudents.sort(key=grade)

for i in s_tudents:
    print(i)
print()


# Tuple of tuples sorting, we need to use sorted which returns a sorted list.
st_udents = (("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr. Krabs", "C", 78),)

sorted_tuples = sorted(st_udents, key=grade)

for i in sorted_tuples:
    print(i)





