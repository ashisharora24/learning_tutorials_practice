
import queue
from sys import setrecursionlimit

def reverseQueue(q1):
    s1 = []
    while q1.empty() is False:
        s1.append(q1.get())
    while len(s1)>0:
        q1.put(s1.pop())

setrecursionlimit(11000)
li = [int(ele) for ele in (input().split()[1:])]
q1 = queue.Queue()
for ele in li:
    q1.put(ele)
reverseQueue(q1)
while(q1.empty() is False):
    print(q1.get(),end= ' ')
