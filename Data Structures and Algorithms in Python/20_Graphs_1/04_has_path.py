# Code : Has Path
# Send Feedback
# Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), check if there exists any path between them or not. Print true or false.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
# Line (E+2) : Two integers v1 and v2 (separated by space)
# Output Format :
# true or false
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# 0 <= v1, v2 <= V-1
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3

# Sample Output 1 :
# true
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :
# false

import queue

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def __str__(self):
        return str(self.adjMatrix)

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def hasMap(self, v1, v2):
        if (self.adjMatrix[v1][v2] > 0 and self.adjMatrix[v2][v1] > 0):
            return True
        q = queue.Queue()
        visited = [False for i in range(self.nVertices)]
        visited[v1] = True
        q.put(v1)
        while q.empty() is False:
            u = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    if i == v2:
                        return True
                    q.put(i)
                    visited[i] = True
        return False


l1 = list(map(int, input().split()))
graph = Graph(l1[0])

for i in range(l1[1]):
    edges = list(map(int, input().split()))
    graph.addEdge(edges[0], edges[1])

l2 = list(map(int, input().split()))
if graph.hasMap(l2[0], l2[1]):
    print ("true")
else:
    print("false")
