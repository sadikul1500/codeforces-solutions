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
	a = cin()
	b = cin()

	maxi = 0
	len_a = len(a)-1
	len_b = len(b)-1
	#print(len_a, len_b)

	for i in range(len_a):
		for j in range(len_a+1):
			if a[i:j] in b:
				maxi = max(j-i, maxi)


	cout(str(len_a + len_b - 2*maxi) + '\n')
	#print(len(a))
	#print(len(b))
	#print(len(a)+ len(b) - 2 * maxi)
	#cout(str(len(a)+ len(b) - 2 * maxi) + '\n')
	