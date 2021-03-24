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

 
#t, = mp()
#for _ in range(t):
n, q, k = mp()
a = mp()
'''
dp = []

for i in range(n-1):
	if i == 0 and i+1 < n:
		dp += [a[i+1] - 1 - 1]
	else:
		dp += [a[i+1] - a[i-1] - 1 - 1]
'''
for __ in range(q):
	l, r = mp()
	count  = 0

	count += a[l-1] - 1 + 2 * (a[r-1] - a[l-1] + 1 - r + l -1) + k - a[r-1]

	'''

	for i in range(l-1, r):
		if i == l-1 and i < r:
			count += a[i+1] - 1 - 1
		elif i == r-1 and i-1 >= l-1:
			count += k - a[i-1] - 1
		else:
			count += a[i+1] - a[i-1] - 1 - 1
	'''

	cout(str(count) + '\n')

