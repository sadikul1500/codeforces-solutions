import sys


import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

output = [0]*n

for i in range(len(l)):
    output[l[i]-1] = i+1 
for val in output:
    print(val, end=' ')
print()