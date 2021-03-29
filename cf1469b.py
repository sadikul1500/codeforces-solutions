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

def myLog(x, y):
	z = int(math.log(x, y))

	if y**(z+1) > x:
		return z
	elif y**(z+1) == x:
		return z+1

#main

 
t, = mp()
for _ in range(t):
	n, k = mp()

	a = set(mp())

	a = sorted(list(a))

	
	x = 0

	for i in range(len(a)):
		if i != a[i]:
			x = i
			break
	else:
		x = max(a) + 1
	
	'''
	for i in range(k):
		if math.ceil((x + max(a))/2) in a:
	'''

	if not k:
		cout(str(len(a)) + '\n')
	elif max(a) + 1 == x:
		cout(str(len(a) + k) + '\n')
	else:
		a += [math.ceil((x+max(a))/2)]
		a = set(a)
		#a.add(math.ceil((x+max(a))/2))
		cout(str(len(a)) + '\n') 





