import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    l1 = []
    l2 = []
    
    summ = sum(a) - s
    
    if summ < 0:
        print(-1)
    
    else:
        for i in range(n):
            if a[i] == 1:
                # if i+1 < n-i:
                l1 += [i+1]
                # else:
                l2 += [n-i]
        l2.sort()
        count = 0
        for i in range(summ):
            if len(l1) > 0 and len(l2) > 0:
                if l1[0] < l2[0]:
                    count += l1[0]
                    for j in range(1, len(l1)):
                        l1[j] -= l1[0]
                    l1.pop(0)
                else:
                    count += l2[0]
                    for j in range(1, len(l2)):
                        l2[j] -= l2[0]
                    l2.pop(0)
            elif len(l1) > 0:
                count += l1[0]
                for j in range(1, len(l1)):
                    l1[j] -= l1[0]
                l1.pop(0)
            else:
                count += l2[0]
                for j in range(1, len(l2)):
                    l2[j] -= l2[0]
                l2.pop(0)
                
        
        print(count)
                    
    
    