# List operations
my_list = [1, 2, 3, 4, 5]
print("Initial list:", my_list)

# Add an element to the list
my_list.append(6)
print("List after adding 6:", my_list)

# Remove an element from the list
my_list.remove(3)
print("List after removing 3:", my_list)

# Modify an element in the list
my_list[2] = 10
print("List after modifying the third element to 10:", my_list)

print()

# Dictionary operations
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Initial dictionary:", my_dict)

# Add an element to the dictionary
my_dict['d'] = 4
print("Dictionary after adding key 'd' with value 4:", my_dict)

# Remove an element from the dictionary
del my_dict['b']
print("Dictionary after removing key 'b':", my_dict)

# Modify an element in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying key 'a' to 10:", my_dict)

print()

# Set operations
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

# Add an element to the set
my_set.add(6)
print("Set after adding 6:", my_set)

# Remove an element from the set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Sets don't support modifying elements directly,
# but you can remove an element and add a new one
my_set.remove(4)
my_set.add(10)
print("Set after removing 4 and adding 10:", my_set)