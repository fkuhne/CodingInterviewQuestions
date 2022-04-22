# https://www.youtube.com/watch?v=vYquumk4nWw
# Given an integer number, compute the Fibonacci sequence as a vector:

# This is too slow! It uses recursion, but computes again repeated numbers.
# The time complexity here is O(2^n)
def fibonacci(n):
    if n == 0: result = 0
    elif n == 1 or n == 2: result = 1
    else: result = fibonacci(n-1) + fibonacci(n-2)
    return result

#print(fibonacci(30))

# To avoid taking too much time (due to repeated computations), let us use memoization,
#  which is basically store intermediate values that will appear again

#lets create a dictionary [int:int] where the key is the position and the value is the Fibobacci number
memo = {}

def memoizedFibonacci(n, memo):
    if n == 0: result = 0
    elif n == 1 or n == 2: result = 1
    elif n in memo: return memo[n]
    else: result = memoizedFibonacci(n-1, memo) + memoizedFibonacci(n-2, memo)
    memo[n] = result
    return result

print(memoizedFibonacci(300, memo))

# The memoized solution has a time complexity of O(2n+1)*O(1) = O(2n+1) = O(n)

# There is another solution with O(n) which uses a bottom-up approach:

def bottomUpFibonacci(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    vector = [0, 1]
    for i in range(2, n+1):
        vector.append(vector[i-1] + vector[i-2])
    return vector[n]
    
print(bottomUpFibonacci(300))