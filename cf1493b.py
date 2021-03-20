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
	h, m = mp()
	hr, mm = cin().split(':')

	#x = ''
	#y = ''

	valid = '01258'
	ref = {'0': '0', '1': '1', '2': '5', '5': '2', '8': '8'}
	'''
	if hr[0] in valid and hr[1] in valid:
		x = ref[hr[0]] + ref[hr[1]]
	if mm[0] in valid and mm[1] in valid:
		y = ref[hr[0]] + ref[hr[1]]

	if x and y and int(x) < h and int(y) < m:
		cout(hr + ':' + mm + '\n')
	'''
	#else:
	p = int(hr)
	q = int(mm)

	a = ''
	b = ''

	for i in range(p, h):
		k = 0
		a = str(i)
		if len(a) == 1:
			a  = '0' + a

		if a[0] in valid and a[1] in valid and int(ref[a[1]] + ref[a[0]]) < m:
			for j in range(q, m):
				b = str(j)
				if len(b) == 1:
					b = '0' + b

				if b[0] in valid and b[1] in valid and int(ref[b[1]] + ref[b[0]]) < h:
					k = 1
					break

		if k:
			break



		else:
			q = 0
	if k:
		cout(a + ':' + b + '\n')
	else:
		cout('00:00\n')



