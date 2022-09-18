import sys
input = sys.stdin.readline
from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = Counter(list(map(int, input().split())))
    
    l = sorted(a.values(), reverse=True)
    #print(l)
    if len(l) == 1:
        if l[0] % 2 == 1:
            print(1)
        else:
            print(0)
        
    else:
        # flag = True
        for i in range(len(l)):
            if l[i] %2 == 1:
                l[i] = 1
            else:
                l[i] = 2
        l2 = Counter(l)
        #print(l2)
        if l2[2] % 2 == 0:
            print(len(l))
        else:
            print(len(l)-1) 
                    
        