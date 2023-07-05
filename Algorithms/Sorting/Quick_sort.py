# Quick Sort is another sorting algorithm which follows divide and conquer approach.
# It requires to chose a pivot, then place all elements smaller than the pivot on the left of the pivot and all elements larger on the right
# Then the array is partitioned in the pivot position and the left and right arrays follow the same procedure until the base case is reached.
# After each pass the pivot element occupies its correct position in the array.
# Time Complexity in Best and Average cases is O(nlog N) whereas in worst case it jumps up to O(n^2). Space complexity is O(log n)
# It is worst in cases where elements are already sorted and you chose the first or last element as pivot.


def Quick_sort(array, start, end):
    ln = len(array)
    if start < end:
        pivot = end
        partitionindex = partition(array, pivot, start, end)

        Quick_sort(array, start, partitionindex -1)
        Quick_sort(array, partitionindex +1, end)
    return array

def partition(array, pivot, start, end):
    pivotvalue = array[pivot]
    partitionindex = start

    for i in range(start, end):
        if array[i] < pivotvalue:
            swap(array, i, partitionindex)
            partitionindex += 1

    swap(array, end, partitionindex)
    return partitionindex

def swap(array, firstindex, secondindex):
    temp = array[firstindex]
    array[firstindex] = array[secondindex]
    array[secondindex] = temp


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# first and last index as 2nd and 3rd parameters
print(Quick_sort(array, 0, len(array) - 1))