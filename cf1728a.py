#input template
from sys import stdin, stdout
from collections import Counter, OrderedDict
import math
cin = stdin.readline
cout = stdout.write
mp = lambda: list(map(int, cin().split()))
 
def chars(): #function for taking string input as character array since string in python is immutable
    s = cin()
    return(list(s[:len(s) - 1]))
 
#print list	
def pl(a):	
	for val in a:
		cout(str(val) + ' ')
	cout('\n')
		
#main
 
 
 
t, = mp()
for _ in range(t):
    n, = mp()
    cnt = mp()

    result = cnt.index(max(cnt))

    cout(str(result+1) + '\n')

