#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating a dictionary
fruits = {'apple': 3, 'banana': 2, 'cherry': 5}

# Adding a new key-value pair
fruits['grape'] = 4

# Updating an existing value
fruits['banana'] = 3

# Accessing values
print(fruits['apple'])  # Output: 3

# Checking if a key exists
if 'banana' in fruits:
    print("Bananas are in the dictionary.")

# Removing an item
del fruits['cherry']
# or
removed_value = fruits.pop('apple')

# Iterating over keys
for key in fruits:
    print(key)

# Iterating over values
for value in fruits.values():
    print(value)

# Iterating over key-value pairs
for key, value in fruits.items():
    print(key, value)


# In[ ]:




