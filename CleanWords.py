
def solution(s:str) -> str:
    list = set()
    seps = set()
    l = s.lower()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            list = list | {i} | {i+1}
        else:
            seps = seps | {i}
    print(list)
    print(seps)
    k = ''
    for n in list:
        k = k + s[n]
    return k
    
a='NatbBbyn'
print(solution(a))

b='asdefFfytrRrRriwytequiwyteXxXXXXxxx'
print(solution(b))

