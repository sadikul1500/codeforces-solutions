# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# n, q = map(int, input().split())

# a = dict(enumerate(map(int, input().split())))

# summ = sum(a.values())
# # b = []
# # d = {}
# #query1 = [0]*(2*10**5)
# # query1Val = [0]*(2*10**5)
# #query2 = -1
# #query2Val = 0
# # flag = 0

# for i in range(q):
#     t = list(map(int, input().split()))
    
#     if t[0] == 1:
#         #a[t[1]-1] = t[2]
#         summ += t[2] - a[t[1]-1]
#         a[t[1]-1] = t[2]
#     else:
#         temp = t[1]
        
#         a = defaultdict(lambda:temp)  #couldn't figure out how it works
#         summ = t[1] * n
#         # query2 = i
#         # query2Val = t[1]
    
#     print(summ)
    
    

    # if t[0] == 1:
    #     if flag == 0:
    #         if t[1]-1 in d.keys():
    #             summ += t[2] - d[t[1] - 1]
    #         else:
    #             summ += t[2] - a[t[1] - 1]
            
            
    #     else:
    #         if t[1]-1 in d.keys():
    #             summ += t[2] - d[t[1] - 1]
    #         else:
    #             summ += t[2] - flag
        
    #     d[t[1]-1] = t[2]
    
    # else:
    #     summ = t[1] * n
    #     flag = t[1]
    
    # print(summ)
    
    # if t[0] == 1:
    #     if len(b) > 0 and b[-2] == t[1]-1:
            
    #     if flag > 0 and b[t[1]-1] == False:
    #         a[t[1]-1] = flag
    #         b[t[1]-1] = True
    #         #summ = summ + t[2] - flag
    #     else:
    #         pass
    #         #summ = summ + t[2] - a[t[1]-1]
    #     summ = summ + t[2] - a[t[1]-1]
    #     #a[t[1]-1] = t[2]
    #     print(summ)
    # else:
    #     summ = t[1]*n
    #     #a = [t[1]]*n
    #     flag = t[1]
    #     #b = [False]*n
    #     print(summ)
    
    
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
 
a = list(map(int, input().split()))
 
summ = sum(a)
# b = []
# d = {}
query1 = [0]*(2*10**5)
query1Val = [0]*(2*10**5)
query2 = -1
query2Val = 0
# flag = 0
 
for i in range(q):
    t = list(map(int, input().split()))
    
    if t[0] == 1:
        if query1[t[1]-1] > query2:
            if query1Val[t[1]-1] == 0:
                query1Val[t[1]-1] = a[t[1]-1]
            summ += t[2] - query1Val[t[1]-1]
        else:
            summ += t[2] - query2Val
        query1[t[1]-1] = i
        query1Val[t[1]-1] = t[2]
    else:
        summ = t[1] * n
        query2 = i
        query2Val = t[1]
    
    print(summ)
    