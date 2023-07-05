# Selection sort involves finding the minimum element in one pass through the array
# and then swapping it with the first position of the unsorted part of the array.
# Time complexity of selection sort is O(n^2) in all cases

def Selection_sort(array):
    count = 0
    for i in range(len(array) - 1): # on last element it will already be sorted
        print(array)
        minimum = array[i]
        min_index = i
        for j in range(i + 1, len(array)): # we go from ith + 1 element to the end
            count += 1
            if array[j] < minimum:
                minimum = array[j]
                min_index = j
        if min_index != i:
            array[min_index], array[i] = array[i], array[min_index]
    
    return f'{array} \nNumber of comparisons = {count}'

arr = [10, 3, 99, 100, 45, 1, 0]
print(Selection_sort(arr))
