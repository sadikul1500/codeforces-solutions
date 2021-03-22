#input template
from sys import stdin, stdout
from collections import Counter, OrderedDict, defaultdict
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
		
def binSearch(l, val, start, end):
	if end < start:
		return False

	mid = (start + end) // 2

	if l[mid] == val:
		return True
	elif l[mid] < val:
		return binSearch(l, val, mid+1, end)
	elif l[mid] > val:
		return binSearch(l, val, start, mid-1)

#main

 
t, = mp()
for _ in range(t):
	n, = mp()
	c = mp()

	a = [0]*3

	for val in c:
		a[val%3] += 1

	move = 0

	a[0] -= n//3
	a[1] -= n//3
	a[2] -= n//3


	if a[0] > 0:
		if a[1] < 0:
			x = min(a[0], abs(a[1]))
			move +=  x* 1
			a[0] -= x
			a[1] += x

		if a[2] < 0 and a[0] > 0:
			x = min(a[0], abs(a[2]))
			move += x * 2
			a[0] -= x
			a[2] += x
	
	if a[1] > 0:
		if a[0] < 0:
			x = min(a[1], abs(a[0]))
			move += x * 2
			a[1] -= x
			a[0] += x

		if a[2] < 0 and a[1] > 0:
			x = min(a[1], abs(a[2]))
			move += x * 1
			a[1] -= x
			a[2] += x

	if a[2] > 0:
		if a[1] < 0:
			x = min(a[2], abs(a[1]))
			move += x * 2
			a[2] -= x
			a[1] += x

		if a[0] < 0 and a[2] > 0:
			x = min(a[2], abs(a[0]))
			move += x * 1
			a[2] -= x
			a[1] += x

	cout(str(move) + '\n')



