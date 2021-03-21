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
		


#main

 
t, = mp()
for _ in range(t):
	x, = mp()

	p = int(x**(1/3))
	k = 0

	for i in range(1, p+1):
		y = x - i*i*i
		z = int(y**(1/3))
		if z > 0 and (z*z*z == y or (z+1)*(z+1)*(z+1) == y):
			cout('Yes\n')
			break
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


