# 1. Sort 10 schools around your house by distance:
# ---> Insertion sort. Very fast on small sorts. Easy to code and has space complexity of O(1). It is also very fast for nearly-sorted or 
#      sorted data.

# 2. eBay sorts listings by the current bid amount:
# ---> Radix or counting sort because we are sorting integers.

# 3. Sport scores on ESPN:
# ---> Quick sort. can be merge sort if there is no problem related to space complexity.

# 4. Massive database (can't fit all into memory) needs to sort through past year's user data:
# ---> Merge sort not quick sort to avoid the worst case of quick sort -> O(n^2)

# 5. Almost sorted Udemy review data needs to update and add 2 new reviews:
# ---> Insertion sort.

# 6. Temperature Records for the past 50 years in Canada:
# ---> QUick sort. or radix/counting sort.

# 7. Large user name database needs to be sorted. Data is very random:
# ---> Merge sort if not worried about memory. or quick sort if not worried about worst case, can get good 
#      pivot and database is not that large.

# 8. You want to teach sorting for the first time:
# ---> Bubble sort. Easy to understand compared to others. Selection sort.