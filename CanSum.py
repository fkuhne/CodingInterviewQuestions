# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=4196s
# Write a function that takes in a target value and an array of numbers as arguments.
# This function should return a boolean indicating wheter or not it is possible
# to generate the target value using numbers of the array
# You may use an element of the array as many times as needed (so that the array can be repeatedly
# used in the recursive calls). You may assume that all input numbers are nonnegative.

#without memoization:
def canSum(target, array):
    if target == 0: return True
    if target < 0: return False

    for num in array:
        remainder = target - num
        if canSum(remainder, array): return True

    return False

# This builds up into a tree with depth equal to the target value (as a worst case scenario)
# and where each node has len(array) as the number of children nodes. So, the time complexity
# would be the time to traverse all this tree, which is O(n^m).

print(canSum(7, [2, 3])) # true
print(canSum(7, [5, 3, 4, 7])) # true
print(canSum(7, [2, 4])) # false
print(canSum(7, [2, 3, 5])) # true
print(canSum(8, [2,3])) # true
print(canSum(300, [7, 14])) # false
