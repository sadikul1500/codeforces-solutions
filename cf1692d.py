import sys
input = sys.stdin.readline
from collections import Counter


def palindrome(st):
    if st[0] == st[-1] and st[1] == st[-2]:
        return True
    return False

t = int(input())

for _ in range(t):
    s = input()
    
    x = int(s.split()[1])
    h = int(s.split()[0].split(':')[0])
    m = int(s.split()[0].split(':')[1])
    
    # print(h,m,x)
    
    h1 = x // 60
    m1 = x % 60
    h2 = h #change it
    m2 = m #change it
    
    count = 0
    total_h = 0
    total_m = 0
    
    while(True):
        hh = str(h2)
        mm = str(m2)
        
        if len(hh) == 1:
            hh = '0' + hh
        if len(mm) == 1:
            mm = '0' + mm
        
        if palindrome(hh+':'+mm)==True:
            count += 1
        
        # print(hh, mm)
        if m2 + m1 > 59:
            m2 = (m2 + m1) % 60
            h2 += 1
        else:
            m2 = m2 + m1
        if h1 + h2 > 23:
            h2 = (h1 + h2) % 24
        else:
            h2 = h1 + h2
            
        # total_m = total_m + m1
        # if total_m > 59:
        #     total_m = total_m % 60
        #     total_h += 1
        
        # total_h = total_h + h1
        # if total_h > 23:
        #     total_h = total_h % 24
        # if total_h == h and total_m == m:
        #     break
        # if total_h >= 72:
        #     break
        if h2 == h and m2 == m:
            break
    
    print(count)
        
        
        
        