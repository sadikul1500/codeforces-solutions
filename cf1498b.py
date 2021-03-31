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
	n, W = mp()

	w = sorted(mp())

	count = [0] * 20

	for wid in w:
		count[int(math.log2(wid))] += 1


	h = 1
	wid = W

	for i in range(n):
		

		k = 0
		for j in range(19, -1, -1):
			if count[j] > 0 and not k:
				k = j
			if 2**j <= wid and count[j] > 0:
				wid -= 2**j
				count[j] -= 1
				break
		else:
			wid = W - 2**k
			count[k] -= 1
			h += 1

	cout(str(h) + '\n')
