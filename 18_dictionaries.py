# dictionary = A changeable, unordered collection of unique key-value pairs
#              Fast because they use hashing.

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals['Germany'])  # Unsafe
print(capitals.get('Germany'))

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'NWO'})
capitals.pop('China')  # Removes this key-value pair.
# capitals.clear()

# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print("Key = " + key + ",", "Value = " + value)



