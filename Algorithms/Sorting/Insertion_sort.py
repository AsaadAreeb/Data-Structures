# In Insertion sort, for the first iteration we fix the first element, assuming it is at its correct position
# Then we loop through the rest of the elements and insert them in their correct positions, with respect to the alreay sorted part of the array
# Time complexity is O(n^2) in worst case
# The best case scenerio is when data is almost sorted or list is small. Time complexity of O(n)

def Insertion_sort(array):
    lenght = len(array)
    select = array[0]
    for i in range(1, lenght):
        print(array)
        if array[i] < select:
            ins = array.pop(i)

            for j in range(0, i):
                if ins < array[j]:
                    array.insert(j, ins)
                    break
        select = array[i]
    
    return array

arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(Insertion_sort(arr))




