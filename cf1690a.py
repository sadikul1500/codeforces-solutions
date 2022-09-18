from re import A


t = int(input())

for _ in range(t):
    n = int(input())
    
    l = []
    l += [n // 3]
    n -= l[0]
    
    l += [n//2]
    l += [n - l[1]]
    
    l = sorted(l)
    
    #for i in range(2):
    if l[0] == l[1]:
        l[0] -= 1
        l[1] += 1
    
    if l[1] == l[2]:
        l[1] -= 1
        l[2] += 1
    
    res = sorted(l)
    
    #res = sorted([a,b,c])
    
    print(res[1], end=' ')
    print(res[2], end=' ')
    print(res[0])
    #c =  