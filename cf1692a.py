t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    count = 0
    
    if b > a:
        count += 1
    if c > a:
        count += 1
    if d > a:
        count += 1
    print(count)