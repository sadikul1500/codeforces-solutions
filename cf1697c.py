import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    
    s = list(input())
    t = list(input())
    # s = li
    
    flag = True
    
    for i in range(n):
        if s[i] == t[i]:
            continue
        elif s[i] == 'a' and t[i] == 'b':
            for j in range(i+1, n):
                if s[j] == 'a':
                    continue
                elif s[j] == 'c':
                    # print('NO')
                    flag = False
                    break
                else:
                    s[j] = 'a'
                    s[i] = 'b'
                    break
            else:
                flag = False
            if flag == False:
                break
        elif s[i] == 'b' and t[i] == 'c':
            for j in range(i+1, n):
                if s[j] == 'b':
                    continue
                elif s[j] == 'a':
                    # print('NO')
                    flag = False
                    break
                else:
                    s[j] = 'b'
                    s[i] = 'c'
                    break
            else:
                flag = False
            if flag == False:
                break
        else:
            flag = False
            break
    
    if flag:
        print('YES')
    else:
        print('NO')