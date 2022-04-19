# Gien an array, find two integers that multiply to 20:

def dp(array, total, index, memo):

    returnValue = 0

    # First element will be also memoized
    if index == 0: memo.append(array[index])
    
    # Went through the end of the array
    if index == len(array): return returnValue
    
    result = total / array[index]

    if result in memo:
        print("Found ({},{})".format(result, array[index]))
        returnValue += 1
    
    print("Appending {} to memo".format(array[index]))
    memo.append(array[index])
    
    # Recursively calls dp for the next element in the array
    returnValue += dp(array, total, index+1, memo)

    return returnValue

def find_solution(array, total):
    memo = []
    r = dp(array, total, 0, memo)
    print("{} pairs have been found.".format(r))

array = [2,4,1,6,5,40,-1, 10]
total = 8

find_solution(array, total)