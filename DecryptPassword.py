def decryptPassword(s):
    # Write your code here
    numberCounter = 0
    
    r = range(len(s))
    for i in reversed(r):
        print("s({}) = {}".format(i,s[i]))
        if s[i] == '0':
            temp = list(s)
            temp[i] = s[0]
            temp = temp[1:]
            s = "".join(temp)
    
        if s[i].isupper() and s[i+1].islower() and s[i+2] == '*':
            temp = list(s)
            temp[i], temp[i+1] = temp[i+1], temp[i]
            temp = temp[:i+2] + temp[i+3:]
            s = "".join(temp)

    return s

print(decryptPassword("51Pa*0Lp*0e"))

print(decryptPassword("43Ah*ck0rr0nk"))


print(sum([1,2,3,4,5]))