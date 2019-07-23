class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def __str__(self):
        return str(self.adjMatrix)

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

graph = Graph(6)
graph.addEdge(0, 1)
graph.addEdge(0, 3)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(2, 3)
graph.addEdge(2, 3)

output = graph.getPath(1, 3)

if output is None:
    pass
else:
    for i in output:
        print(i, end= " ")
