# Lineary searching for something in list is not the fastest way to do this, but can we improve it, how about if the list is sorted like this:
# [1, 3, 6, 45, 77, 124, 200]
# whats the better way to go about it:
# answer to that question is Binary search: In binary search because we know list is sorted, we can discard half the items instead one at a time
# Ex: let's say we are looking for 124 in list, we will start from the middle and check if that element is higher or lower than 124, as we can
# see 45 is lower than 124 so we can discard everything to the left to it [right,if higher]. Then we go to the middle index again and repeat 
# the steps.
# It is also called divide and conquer approach. This approach always has O(log n) time complexity.