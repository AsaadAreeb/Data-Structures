# Algorithm     Average     Worst case
# Space         O(n)        O(n)
# Search        O(n)        O(n)
# Insert        O(n)        O(n)
# Delete        O(n)        O(n)


# In computer science, a trie, also called digital tree or prefix tree, is a type of k-ary search tree, a tree data structure used for locating 
# specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual 
# characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links 
# between nodes, which represent each character in the key.

# Unlike a binary search tree, nodes in the trie do not store their associated key. Instead, a node's position in the trie defines the key with 
# which it is associated. This distributes the value of each key across the data structure, and means that not every node necessarily has an 
# associated value.

# All the children of a node have a common prefix of the string associated with that parent node, and the root is associated with the empty 
# string. This task of storing data accessible by its prefix can be accomplished in a memory-optimized way by employing a radix tree.


                                        #                 |Empty String|
                                        #              /        |         \
                                        #           t /       A |          \ i
                                        #            /          |           \ 
                                        #          [t]         [A]           [i]
                                        #      o /     \ e                     \ n
                                        #       /       \                       \
                                        #   [to]         [te]                    [in]
                                        #              /   | \                   /
                                        #           a /  d |  \ n             n /
                                        #            /     |   \               /
                                        #       [tea]    [ted]  [ten]      [inn]