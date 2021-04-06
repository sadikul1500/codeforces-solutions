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

def isPalindrome(s):
    return s == s[::-1]



#main

 
t, = mp()
for _ in range(t):
	n, = mp()
	a = sorted(mp())[::-1]

	alice = 0
	bob = 0
	for i in range(n):
		if i % 2: #bob
			if a[i] % 2:
				bob += a[i]
		else:
			if not a[i] % 2:
				alice += a[i]

	if alice > bob:
		cout('Alice\n')
	elif bob > alice:
		cout('Bob\n')
	else:
		cout('Tie\n')

