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
a = []

a = {i**3 for i in range(1, 10000)}

for _ in range(t):
	x, = mp()

	#p = int(x**(1/3))
	#k = 0
	'''
	for val in a:
		if val > x:
			cout('No\n')
			break
		if binSearch(a, x-val, 0, 9999):
			cout('Yes\n')
			break
	'''
	for val in a:
		if x-val in a:
			cout('Yes\n')
			break
	#for i in range(1, p+1):
	#	y = x - i*i*i
		'''
		z = int(y**(1/3))
		if z > 0 and (z*z*z == y or (z+1)*(z+1)*(z+1) == y):
			cout('Yes\n')
			break
		'''
	#	if binSearch(a, y, 0,9999):
	#		cout('Yes\n')
	#		break
	else:
		cout('No\n')
	'''

	for i in range(1, p+1):
		for j in range(i, p+1):
			if 3*(math.log(i) + math.log(j)) == math.log(x):
				cout('YES\n')
				k = 1
				break
		if k:
			break

	else:
		cout('NO\n')
	'''


