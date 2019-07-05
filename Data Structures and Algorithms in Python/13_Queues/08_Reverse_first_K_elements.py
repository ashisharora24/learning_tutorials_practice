
import queue


def reverseFirstK(q, k):
    l1 = []
    q2 = queue.Queue()
    #check_condtion = False
    if k > 0:
        while q.empty() is False:
            if k > 0:
                l1.append(q.get())
            else:
                q2.put(q.get())
            k -= 1
    while len(l1) > 0:
        q.put(l1.pop())
    while q2.empty() is False:
        q.put(q2.get())

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k)
while(q.qsize()>0):
	print(q.get())
	n-=1
