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
	n, = mp()
	a = Counter(mp())

	#d = defaultdict(int)

	'''
	for i in range(n):
		#if a[i] in d:
		d[a[i]] += 1
		#else:
		#	d[a[i]] = 1
	'''

	s = sorted(a.values())
	l = len(s)
	#for val in d.values():
	#	s.add(val)

	ans  = 1e9+1
	summ = sum(s)
	#print(122, s)

	for i in range(l):
		ans = min(ans, summ - s[i] * (l-i))
		
	cout(str(ans) + '\n')



