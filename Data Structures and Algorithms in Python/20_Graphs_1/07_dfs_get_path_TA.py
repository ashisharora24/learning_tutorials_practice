import queue
class Graph:
    def __init__(self,v):
        self.v=v
        self.m=[[0 for i in range(v)] for j in range(v)]
    def addEdge(self, v1, v2):
        self.m[v1][v2] = 1
        self.m[v2][v1] = 1

    def __getPathDfs(self, v1, v2, visited):
        visited[v1] = True
        if v1 == v2:
            return [v2]

        for i in range(self.nVertices):
            if (self.adjMatrix[v1][i] > 0 and visited[i] is False):
                output = self.__getPathDfs(i, v2, visited)
                if output is None:
                    pass
                else:
                    output.append(v1)
                    return output
        return None



    def getPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__getPathDfs(v1, v2, visited)


v, e = [int(x) for x in input().split()]
g=Graph(v)

for i in range(e):
    a,b=[int(x) for x in input().split()]
    g.addEdge(a,b)

x,y=[int(x) for x in input().split()]
g.getPath(x,y)
