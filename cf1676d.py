import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    a = []
    
    for _ in range(n):
        a += [list(map(int, input().split()))]
    #print(a)
    
    maxi = 0
    d = defaultdict(lambda:0)
    d2 = defaultdict(lambda:0)
    
    for i in range(n):
        for j in range(m):
            d[i+j] += a[i][j]
            d2[i-j] += a[i][j]
    
    for i in range(n):
        for j in range(m):
            summ = d[i+j] + d2[i-j] - a[i][j]#a[i][j]
            # p = i+1
            # q = j+1
            # while p < n and q < m:
            #     summ += a[p][q]
            #     p += 1
            #     q += 1
            # p = i-1
            # q = j-1
            
            # while p > -1 and q > -1:
            #     summ += a[p][q]
            #     p -= 1
            #     q -= 1
            # p = i-1
            # q = j+1
            # while p > -1 and q < m:
            #     summ += a[p][q]
            #     p -= 1
            #     q += 1
            # p = i+1
            # q = j-1
            # while p < n and q > -1:
            #     summ += a[p][q]
            #     p += 1
            #     q -= 1
            if summ > maxi:
                maxi = summ
            #print(summ, i, j)
    
    print(maxi)