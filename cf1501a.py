#input template
from sys import stdin, stdout
from collections import Counter, OrderedDict
import math
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
		
#main
 
 
 
t, = mp()
for _ in range(t):
	n, = mp()
	a = []

	for i in range(n):
		a += [mp()]
	#pl(a)
	t = mp()

	z = a[0][0]
	d = 0
	p = 0

	for i in range(n):
		p = d + z + t[i]

		if a[i][1] - p >= math.ceil((a[i][1]-a[i][0])/2):
			d = a[i][1]
		else:
			d = p + math.ceil((a[i][1]-a[i][0])/2)

		if i < n-1:
			z = a[i+1][0] - a[i][1]

	cout(str(p) + '\n')

