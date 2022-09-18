import math

n, k = map(int, input().split())

if k <= math.ceil(n/2):
    print(k*2-1)
else:
    print((k - math.ceil(n/2))*2)