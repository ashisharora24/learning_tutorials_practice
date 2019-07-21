# Code : BFS Traversal
# Send Feedback
# Given an undirected and connected graph G(V, E), print its BFS traversal.
# Here you need to consider that you need to print BFS path starting from vertex
# 0 only.
# V is the number of vertices present in graph G and vertices are numbered from
# 0 to V-1.
# E is the number of edges present in graph G.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting
# that there exists an edge between Vertex 'a' and Vertex 'b'.
# Output Format :
# BFS Traversal (separated by space)
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# 0 1 3 2
# Download Test Casesimport queueimport queue
import queue

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

        q = queue.Queue()
    def __str__(self):
        return str(self.adjMatrix)

    def bfs(self):
        q = queue.Queue()
        q.put(0)
        visited = [False for i in range(self.nVertices)]
        visited[0] = True
        while q.empty() is False:
            u = q.get()
            print(u, end=" ")
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
    # def __bfsHelper(self, q, visited):
    #     sv = q.get()
    #     if visited[sv] is False:
    #         print(sv, end=" ")
    #         visited[sv] = True
    #         for i in range(self.nVertices):
    #             if (self.adjMatrix[sv][i] > 0 and visited[i] is False):
    #                 q.put(i)
    #         if q.empty() is False:
    #             self.__bfsHelper(q, visited)
    #
    # def bfs(self):
    #     visited = [False for i in range(self.nVertices)]
    #     q = queue.Queue()
    #     q.put(0)
    #     self.__bfsHelper(q, visited)

    def cotainsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.cotainsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0


# li = [int(ele) for ele in input().split()]
# g = Graph(li[0])
# #print(li[0], li[1])
# for i in range(li[1]):
#     edges = [int(ele) for ele in input().split()]
# #    print(edges[0], edges[1])
#     g.addEdge(edges[0], edges[1])
# print("---------------------")
# g.bfs()
# # -------------------------------------------


l1 = list(map(int, input().split()))
graph = Graph(l1[0])

for i in range(l1[1]):
    edges = list(map(int, input().split()))
    graph.addEdge(edges[0], edges[1])
graph.bfs()
