#input template
from sys import stdin, stdout
from collections import Counter, OrderedDict
import math
import re
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
	n, u, v = mp()
	a = mp()

	cnt = 0

	for i in range(1, n):
		if abs(a[i] - a[i-1]) == 0:
			continue
		elif abs(a[i] - a[i-1]) > 1:
			cout('0\n')
			break
		else:
			cnt = 1
			#cout(str(min(u, v)) + '\n')
			#break
	else:
		if cnt :
			cout(str(min(u, v)) + '\n')
		else:
			cout(str(v + min(u, v)) + '\n')

