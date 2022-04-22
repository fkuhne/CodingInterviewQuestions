# Compute most frequent number:

def ComputeMostFreq(array, memo, currentMax):
    for n in array:
        memo[n] += 1
    
        if memo[n] > currentMax[1]:
            currentMax = [n, memo[n]]

    return memo, currentMax

array = [1, 3, 1, 3, 2, 1, 3, 3, 0, 0, 0, 0, 0]
memo =  dict.fromkeys(array, 0)
mostFreq = [array[0], 1]

freqDict, mostFreq = ComputeMostFreq(array, memo, mostFreq)

print("The frequency vector is {}".format(freqDict))
print("The most frequent element is {}, which appears {} times.".format(mostFreq[0], mostFreq[1]))
