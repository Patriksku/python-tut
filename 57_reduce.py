# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements, and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
# letters = ["HE", "L", "L", "O"]
# letters = ["HEL", "L", "O"]
# etc.

word = functools.reduce(lambda x, y: x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
fact_of5 = functools.reduce(lambda x, y: x * y, factorial)
print(fact_of5)








