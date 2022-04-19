# https://www.youtube.com/watch?v=nqlNzOcnCfs
# Dynamic Programming Interview Question #1 - Find Sets Of Numbers That Add Up To 16

# Assuming that array is sorted, has only integer, unique, positive numbers

# recursion with "memoization":
def dp(array, total, index, memo):

    key = "{},{}".format(total, index)
    
    if key in memo: return memo[key]
    
    if total == 0: return 1 # the empty set {}
    elif total < 0: return 0
    elif index < 0: return 0

    if total < array[index]:
        returnValue = dp(array, total, index-1, memo)
    else:
        returnValue = dp(array, total-array[index], index-1, memo) + dp(array, total, index-1, memo)
    
    memo[key] = returnValue

    return returnValue


# recursion but without memoization:
def rec(array, total, index):
    if (total == 0): return 1 # the empty set {}
    elif (total < 0): return 0
    elif (index < 0): return 0

    # no we go for the actual recursive cases:

    if total < array[index]:
        # if we are here, the given total value is already less than the current array element,
        #  there would be no way of finding a subset out of these elements that add up to total
        #  which includes the current item. So we can call the recursion again but for the next
        #  element (index-1)
        return rec(array, total, index-1)
    
    else:
        # here we have the two branches going down the tree:
        #  N (which is the result of this problem) would be the sum of the number of subsets that
        #  adds up to total which includes array[index] AND the sum of the number of subsets that
        #  adds up to total which DO NOT includes array[index]
        return rec(array, total, index-1) + rec(array, total-array[index], index-1)

def count_sets_dp(array, total):
    memo = {}
    return dp(array, total, len(array)-1, memo)
    #return rec(array, total, len(array)-1)


array = [2, 4, 6, 10]
total = 16

print(count_sets_dp(array, total))
