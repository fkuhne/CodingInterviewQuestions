#https://www.algoexpert.io/questions/Validate%20Subsequence

def dp(array, sequence, index, memo):
	if len(sequence) == 0 or sequence is None: return False
	
	if len(array) == 0 or index > (len(sequence) - 1): return sequence == memo	
	
	if array[0] != sequence[index]:
		# if the current first array element is not expected, discard it
        # and repeat the call, for the same sequence index
		return dp(array[1:], sequence, index, memo)
	else:
        # if the array element is equal to the current expected element
        # in the sequence, add it to the memo and repeat the call, now
        # incrementing the sequence index and also discarding the first
        # array element
		memo.append(sequence[index])
		return dp(array[1:], sequence, index+1, memo)

def isValidSubsequence(array, sequence):
    # Write your code here.
    memo = []
    return dp(array, sequence, 0, memo)

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [25])) # expected True

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [22,25,6])) # expected True

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [25, 22])) # expected False
