# In computer science, a heap is a specialized tree-based data structure that satisfies the heap property: In a max heap, for any given node C, 
# if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than 
# or equal to the key of C. The node at the "top" of the heap (with no parents) is called the root node.

# The heap is one maximally efficient implementation of an abstract data type called a priority queue, and in fact, priority queues are often 
# referred to as "heaps", regardless of how they may be implemented. In a heap, the highest (or lowest) priority element is always stored at 
# the root. However, a heap is not a sorted structure; it can be regarded as being partially ordered. A heap is a useful data structure when 
# it is necessary to repeatedly remove the object with the highest (or lowest) priority, or when insertions need to be interspersed with removals 
# of the root node.


    #             100  
    #          /       \
    #        19         36
    #       /  \       /  \
    #     17    3     25   1
    #    /  \
    #   2    7
# A common implementation of a heap is the binary heap, in which the tree is an almost complete binary tree (see figure). The heap data structure, 
# specifically the binary heap, was introduced by J. W. J. Williams in 1964, as a data structure for the heapsort sorting algorithm. Heaps are 
# also crucial in several efficient graph algorithms such as Dijkstra's algorithm. When a heap is a complete binary tree, it has the smallest 
# possible height—a heap with N nodes and a branches for each node always has loga N height.

# Note that, as shown in the graphic, there is no implied ordering between siblings or cousins and no implied sequence for an in-order traversal 
# (as there would be in, e.g., a binary search tree). The heap relation mentioned above applies only between nodes and their parents, 
# grandparents, etc. The maximum number of children each node can have depends on the type of heap.


# Heaps are usually implemented with an array, as follows:

# Each element in the array represents a node of the heap, and
# The parent / child relationship is defined implicitly by the elements' indices in the array.

# For a binary heap, in the array, the first index contains the root element. The next two indices of the array contain the root's children. 
# The next four indices contain the four children of the root's two child nodes, and so on. Therefore, given a node at index i, its children are 
# at indices 2i + 1 and 2i + 2 and its parent is at index ⌊(i−1)/2⌋. This simple indexing scheme makes it efficient to move "up" or "down" the 
# tree.

# [100, 19, 36, 17, 12, 25, 5, 9, 15, 6, 11, 13, 8, 1, 4]

# 100___________
#        |     |
#       19     36_________________________
#        ---------------         |       |
#               |      |         |       |
#               17     12        25      5_________________________________________________________________________________
#               |      |         ------------------------------------------------------------------               |       |
#               |      -----------------------------------------------                 |          |               |       |
#               ---------------------------            |             |                 |          |               |       |
#                               |         |            |             |                 |          |               |       |
#                               9         15           6             11                13         8               1       4