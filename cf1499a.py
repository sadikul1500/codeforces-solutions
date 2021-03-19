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
	n, k1, k2 = mp()
	w, b = mp()

	wh = max(0, w-min(k1,k2))
	bl = max(0, b-n+max(k1,k2))

	diff = max(k1,k2) - min(k1,k2)

	if bl*2 <= diff and wh*2 <= diff:
		cout('YES\n')
	else:
		cout('NO\n')



	#cout(str(cnt) + '\n')



	
	
	#cout(str(p) + '\n')

