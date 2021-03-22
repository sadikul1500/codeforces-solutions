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
	a = mp()

	d = defaultdict(list)

	for i in range(n):
		d[a[i]].append(i + 1)

	a.sort()

	l = []
	temp = 0
	y = d[max(a)][-1]

	for i in range(n-1):
		if a[i] + temp >= a[i+1]:
			if d[a[i]]:
				l += [d[a[i]][0]]
				d[a[i]].remove(d[a[i]][0])
		else:
			l.clear()

		temp += a[i]

	l += [y]
	l.sort()

	cout(str(len(l)) + '\n')
	pl(l)


	