# Merge Sort uses the Divide and Conquer approach. It involves breaking up the array from the middle until
# Arrays of only 1 elements remain and thein merging them back up in a sorted order.
# Time complexity is O(nlog N) and space complexity is O(n)

import math

def Merge_sort(array):
    if len(array) == 1:
        return array
    
    length = len(array)
    middle = math.floor(length / 2)
    left = array[:middle]
    right = array[middle:]
    # print('Left {}'.format(left))                     # uncomment them to see how array is splitted
    # print('Right {}'.format(right))

    return merge(Merge_sort(left), Merge_sort(right))

def merge(left, right):
    result = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    # print(left, ' ', right)                           # uncomment them to see how array is merged back
    # print( result + left[leftindex:] + right[rightindex:] )

    return result + left[leftindex:] + right[rightindex:]




array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

merger = Merge_sort(array)

print(merger)