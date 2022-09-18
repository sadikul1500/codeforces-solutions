import sys
input = sys.stdin.readline
from collections import Counter
t = int(input())

for _ in range(t):
    blank = input()
    s = []
    for i in range(8):
        s += [input()]
    
    for i in range(1, 7):
        for j in range(1, 7):
            if s[i][j] == '#':
                if s[i-1][j-1] == '#' and s[i-1][j+1] == '#' \
                    and s[i+1][j-1] == '#' and s[i+1][j+1] == '#':
                        print(i+1, j+1)
                        break
                        