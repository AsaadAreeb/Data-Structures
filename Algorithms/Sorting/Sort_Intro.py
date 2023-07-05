letters = ['a', 'd', 'r', 'e', 'b', 'z']

numbers = [2, 65, 34, 2, 1, 7, 8]

spanish = ['único', 'árbol', 'cosas', 'fútbol']

# letters.sort()
# print(letters)

# numbers.sort()
# print(numbers)

# spanish.sort()
# print(spanish)

# The reason the sorting result is not as expected is due to the default sorting behavior in Python, which is based on lexicographic order. 
# In lexicographic order, uppercase letters come before lowercase letters, and diacritical marks (such as accents) are not taken into account. 
# To sort the list correctly, you can use the "sorted()" function along with a custom key function that takes into account the specific sorting 
# requirements for Spanish words. One way to achieve this is by utilizing the "locale" module in Python. Here's an example:

import locale

# Set the locale to Spanish
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

# List of Spanish words
spanish = ['único', 'árbol', 'cosas', 'fútbol']

# Sort the list using a custom key function
sorted_spanish = sorted(spanish, key=locale.strxfrm)

print(sorted_spanish)