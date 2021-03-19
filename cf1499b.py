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
	s = cin()
	n = len(s)
	
	x = 500
	y = 0

	for i in range(n-1):
		if s[i:i+2] == '11':
			x = i
			break

	for i in range(n-2,1,-1):
		if s[i:i+2] == '00':
			y = i
			break
	if y > x:
		cout('no\n')
	else:
		cout('yes\n')


	



	'''
	for i in range(len(s)):


	for i in range(len(s)):
		if s[i] == '1':
			l += [i]

	if len(l) == 0 or len(l) == len(s):
		cout('Yes\n')
	elif len(l) + 1 == len(s) and s[-1] == '0':
		cout('yes\n')
	else:
		for i in range(len(l)):

	'''



	#cout(str(cnt) + '\n')



	
	
	#cout(str(p) + '\n')

