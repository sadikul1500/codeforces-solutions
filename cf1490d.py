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
		

d = [-1]*101

def depth(l, dep):
	global d
	maxi = max(l)

	ind = l.index(maxi)
	indd = a.index(maxi)
	
	d[indd] = dep

	return l[:ind], l[ind+1:]

def manipulate(l, dep):
	if not l:
		return
	x, y = depth(l,dep)

	if x:
		manipulate(x, dep+1)
	if y:
		manipulate(y, dep+1)





#main

 
t, = mp()
for _ in range(t):
	n, = mp()
	a = mp()

	manipulate(a, 0)

	pl(d[:n])



