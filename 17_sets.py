# Set = Collection which is unordered, un-indexed. No duplicate values allowed.
# --> Faster than a list if we want to check if something is in it.
# --> Comparing sets for commons/differences 

utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)  # Adds another set into the set.

dinner_table = utensils.union(dishes)  # Creates a new set with items from the specified sets.

# for x in utensils:
#     print(x)

# Not the same as the reversed scenario.
# print(dishes.difference(utensils))  # What dishes contain that utensils does not.


print(dishes.intersection(utensils))  # What dishes contains that utensils also contains.

for x in dinner_table:
    print(x)
























