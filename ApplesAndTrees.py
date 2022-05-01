# https://www.hackerrank.com/challenges/apple-and-orange/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    inRange = range(s,t+1)
    inApples = 0
    inOrange = 0
    for apple in apples:
        if (a + apple) in inRange: inApples += 1
    
    for orange in oranges:
        if (b + orange) in inRange: inOrange += 1
    
    print(inApples)
    print(inOrange)


countApplesAndOranges(7, 11, 5, 15, [-2,2,1], [5,-6])
