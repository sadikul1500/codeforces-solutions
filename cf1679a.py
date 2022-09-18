t = int(input())

for _ in range(t):
    n = int(input())
    x, y = 0, 0
    
    if n<4 or n%2 ==1:
        print(-1)
    elif n%12 == 0:
        print(n//6, n//4)
    elif n%6 == 0:
        print(n//6, (n-6)//4 + 1)
    elif n%4 == 0 or n%2==0:
        #print(n//4, end=' ')
        if n-4 > 0 and (n-4)%6 == 0:
            print((n-4)//6 +1, end=' ')
        elif n-8 > 0 and (n-8)%6 == 0:
            print((n-8)//6 +2, end=' ')
        else:
            print(n//4, end=' ')
        print(n//4)
            
    else:
        print(-1)
    
    # elif n%2 == 0 and n>=4:
    #     print(n//4, )
    # if n%6 == 0:
    #     x = n // 6
    # if n%4 == 0:
    #     y = n // 4
    
    # if x == 0 and y == 0:
    #     print(-1)
    # elif x == 0 or y == 0:
    #     print(max(x,y), max(x,y))
    # else:
    #     print(x, y)