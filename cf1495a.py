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
	#s = cin()
	#n = len(s)
	n, = mp()
	
	x = []
	y = []

	for i in range(2*n):
		a, b = mp()
		if a == 0:
			x += [abs(b)]
		else:
			y += [abs(a)]

	x.sort()
	y.sort()

	summ = 0.0

	for i in range(n):
		summ += (x[i]*x[i] + y[i]*y[i]) ** .5

	cout(str(summ) + '\n')


