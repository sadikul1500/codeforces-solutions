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

 
#t, = mp()
#for _ in range(t):
n, m = mp()
s = []
for i in range(n):
	s += [chars()]
#print(s[1][1])

for i in range(n):
	for j in range(m):
		temp = 1
		if s[i][j] == '.':
			if i+1 < n:
				if s[i+1][j] == '*':
					cout('no\n')
					temp = 0
					break
			if i-1 >= 0:
				if s[i-1][j] == '*':
					cout('no\n')
					temp = 0
					break
			if j+1 < m:
				if s[i][j+1] == '*':
					cout('no\n')
					temp = 0
					break
			if j-1 >= 0:
				if s[i][j-1] == '*':
					cout('no\n')
					temp = 0
					break
			if i+1 < n and j-1 >= 0:
				if s[i+1][j-1] == '*':
					cout('no\n')
					temp = 0
					break

			if i+1 < n  and j+1 < m:
				if s[i+1][j+1] == '*':
					cout('no\n')
					temp = 0
					break
			if i-1 >= 0 and j+1 < m:
				if s[i-1][j+1] == '*':
					cout('no\n')
					temp = 0
					break
			if i-1 >= 0 and j-1 >= 0:
				if s[i-1][j-1] == '*':
					cout('no\n')
					temp = 0
					break
			

		elif s[i][j] != '*':
			k = int(s[i][j])
			cnt = 0

			if i+1 < n:
				if s[i+1][j] == '*':
					cnt += 1
			if i-1 >= 0:
				if s[i-1][j] == '*':
					cnt += 1
			if j+1 < m:
				if s[i][j+1] == '*':
					cnt += 1
			if j-1 >= 0:
				if s[i][j-1] == '*':
					cnt += 1
			if i+1 < n and j-1 >= 0:
				if s[i+1][j-1] == '*':
					cnt += 1

			if i+1 < n  and j+1 < m:
				if s[i+1][j+1] == '*':
					cnt += 1
			if i-1 >= 0 and j+1 < m:
				if s[i-1][j+1] == '*':
					cnt += 1
			if i-1 >= 0 and j-1 >= 0:
				if s[i-1][j-1] == '*':
					cnt += 1
			

			if cnt != k:
				cout('no\n')
				#print(i,j, cnt, k)
				temp = 0
				break
	if not temp:
		break
else:
	cout('yes\n') 





