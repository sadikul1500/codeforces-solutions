import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    l = []
    for i in range(n):
        l += [i+1]  
    for i in range(n):
        if i == n-1:
            if l[i] == i+1:
                print(-1)
                break
        elif s[i] == s[i+1]:
            #temp = l[i]
            l[i], l[i+1]= l[i+1], l[i]
            #l[i+1] = 
        elif l[i] == i+1:
            print(-1)
            break
    else:
        for val in l:
            print(val, end=' ')
        print()
            
            
    # if n%2 == 1:
    #     x = Counter(s)
    #     #print(max(x.values()))
    #     if len(x) == 1:
    #         print(n, end=' ')
    #         for i in range(1, n):
    #             print(i, end=' ')
    #     else:
    #         print(-1, end=' ')
    # else:
    #     for i in range(n-1, 0, -2):
    #         if s[i] == s[i-1]:
    #             continue
    #         else:
    #             print(-1, end=' ')
    #             break
    #     else:
    #         #l = []
    #         for i in range(1, n+1):
    #             if i%2 == 1:
    #                 print(i+1, end=' ')
    #             else:
    #                 print(i-1, end=' ')
    # print()