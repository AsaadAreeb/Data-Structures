# Linear search can be simply explained by this:
# we have a list [6, 12, 3, 5 9, 46] (it can be anything)
# we go one by one looking through list for the item we want
# best case scenario would be 'we find what we are looking for in O(1)' it is at the very begining of the list
# worst case would be O(n), we have to traverse the whole list.
# even if the item doesn't exist we stil have to check every single item in the list.


a_list = ['centaur', 'godzilla', 'mosura', 'minotaur', 'hydra', 'nessie']
index = a_list.index('mosura')

print(index)

print('mosura' in a_list)