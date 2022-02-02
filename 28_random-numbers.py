import random

x = random.randint(1, 6)  # Random number 1 - 6 (like a dice)
y = random.random()  # Random float between 0 and 1.
print(x)
print(y)


# This will generate a random choice from a list!
myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print(z)


# This will shuffle the elements in a list!
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)


