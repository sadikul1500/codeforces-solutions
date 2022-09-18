t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    s = []
    
    for _ in range(n):
        s += [input()]
    
    minx = miny = 0
    flag = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 'R':
                minx = i
                miny = j
                flag = 1
                break
            
        if flag:
            break
        
    flag = 0    
    for i in range(minx+1,n):
        for j in range(0, miny):
            if s[i][j] == 'R':
                #print('NO')
                flag = 1
                break
    
    if flag == 0:
        print('YES')
    else:
        print('NO')
        
            