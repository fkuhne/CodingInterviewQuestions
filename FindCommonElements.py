# Given two arrays, return a third array with the common elements beween them:

def findCommon(A, B, memo):

    startVec = A if len(A) < len(B) else B
    otherVec = B if len(A) < len(B) else A

    for i in range(len(startVec)):
        if startVec[i] in otherVec:
            memo.append(startVec[i])
            otherVec.remove(startVec[i])
            print("otherVec = {}".format(otherVec))

    print(memo)
    return memo

A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10, 3]
memo = []

findCommon(A, B, memo) # expected result: [1, 4, 9]
