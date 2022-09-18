t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    summ = sum(a)
    
    for val in a:
        if val * (n-1) == summ - val:
            print('yEs')
            break
    else:
        print('nO')