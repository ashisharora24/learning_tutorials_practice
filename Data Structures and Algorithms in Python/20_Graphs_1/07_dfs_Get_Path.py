class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def __str__(self):
        return str(self.adjMatrix)

    def __dfsHelper(self, cv, v, visited):
        # print("cv : ", cv)
        # print("v : ", v)
        # print("visited : ", visited)
        visited[cv] = True
        if self.adjMatrix[cv][v] > 0:
            if cv == 0:
                return [v], visited
            return [v, cv], visited
        else:
            for i in range(self.nVertices):
                # print([cv],[i]," : ", self.adjMatrix[cv][i])
                if (self.adjMatrix[cv][i] > 0 and visited[i] is False):
                    # print("------------")
                    # print(" cv : ", cv)
                    # print(" i : ", i)

                    if i == v:
                        visited[i] = True
                        return [i, cv], visited
                    output, visited = self.__dfsHelper(i, v, visited)
                    if output is None:
                        pass
                    else:
                        output.append(cv)
                        return output, visited
        return None, visited


    def dfs(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        if (v1 == 0 and v2 != 0):
            # print("DFS Case 1")
            output, visited = self.__dfsHelper(0, v2, visited)
            # print("Output : ", output)
            if output is None:
                return None
            return output[::-1]
        elif (v1 != 0 and v2 == 0):
            # print("DFS Case 2")
            output, visited = self.__dfsHelper(0, v1, visited)
            # print("Output : ", output)
            if output is None:
                return None
            return output
        else:
            # print("DFS Case 3")
            output1, visited = self.__dfsHelper(0, v2, visited)
            # print("Output1 : ", output1)
            if output1 is None:
                return None
            else:
                visited = [False for i in range(self.nVertices)]
                for i in output1:
                    visited[i] = True
                output2, visited = self.__dfsHelper(0, v1, visited)
                # print("Output2 : ", output2)
                if output2 is None:
                    return None
                else:
                    if len(output1) == 1:
                        output1.append(0)
                    output1.extend(output2[1::-1])
                    # print("Output1 : ", output1)
                    return output1

    def getPath(self, v1, v2):
        if v1 == v2:
            # print("GetPath Case 1")
            return None
        elif self.adjMatrix[v1][v2] > 0:
            # print("GetPath case 2")
            return [v2, v1]
        else:
            # print("GetPath case 3")
            return self.dfs(v1, v2)

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
