# In Bubble Sort, the largest value is bubbled up in every pass.
# Every two adjacent items are compared and they are swapped if they are in the wrong order.
# This way, after every pass, the largest element reaches to the end of the array.
# Time complexity of Bubble Sort in Worst and Average Case is O(n^2) and in best case, its O(n)

def bubble_sort(array):
    count = 0

    for i in range(len(array) - 1): # we don't need to sort last element
        print(array)
        for j in range(len(array) - i - 1): # in every interation of outer loop one number gets sorted, so inner loop will only run for unsorted
            count += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return f'{array} \nNumber of comparisons = {count}'

arr = [5, 9, 3, 10, 45, 2, 0]
print(bubble_sort(arr))


def betterLooking_bubble_sort(array):
    count = 0
    while count < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        count += 1
    return f'Sorted array {array}'

# arr = [5, 9, 1, 2, 7, 3, 8, 2]
# print(betterLooking_bubble_sort(arr))