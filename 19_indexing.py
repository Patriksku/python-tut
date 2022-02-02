# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "patrik Skuza!"

if name[0].islower():
    name = name.title()

print(name)


first_name = name[:6].upper()
last_name = name[7:].lower()
last_char = name[-1]  # Last element. We can move "backwards" by using the "-" sign.

print(first_name)
print(last_name)
print(last_char)





















