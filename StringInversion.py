# Time complexity is O(n/2), because it goes only until the middle of the string


def invert(s):
    n = len(s)
    stringAsList = list(s)
    for i in range(int(n/2)):
        #print("before: s[{}] = {} / s[{}-{}] = {}".format(i, stringAsList[i], n-1, i, stringAsList[n-1-i]))
        stringAsList[i], stringAsList[n-1-i] = stringAsList[n-1-i], stringAsList[i]
        #print("after:  s[{}] = {} / s[{}-{}] = {}".format(i, stringAsList[i], n-1, i, stringAsList[n-1-i]))
    
    return "".join(stringAsList)

print("pirulito is {}".format(invert("pirulito"))) # otilurip
print("chimarrao is {}".format(invert("chimarrao"))) # oarramihc