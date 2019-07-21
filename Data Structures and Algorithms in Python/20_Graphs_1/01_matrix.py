class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        print(self.adjMatrix)

    def __str__(self):
        return str(self.adjMatrix)

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


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(2, 1)
g.addEdge(2, 2)
print(g)
