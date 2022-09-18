#python is ridiculous
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if a[j] <= a[i]:
                count += 1
    
    print(count) 