# NOMES: Pedro Porto, Gabriel Bessa

from tabulate import tabulate
from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = []
        self.nodes = []

    def insertNode(self, node):
        self.nodes.append(node)

        for row in self.graph:
            row.append(0)

        self.graph.append([ 0 for i in range(len(self.graph) + 1) ])

    def insertPath(self, sourceIndex, destIndex, weight = 1, directed = True):
        if len(self.graph) < sourceIndex or len(self.graph) < destIndex:
            print("Posições inválidas")
            return

        self.graph[sourceIndex][destIndex] = weight

        if not directed:
            self.graph[destIndex][sourceIndex] = weight

    def removePath(self, sourceIndex, destIndex, directed = True):
        if len(self.graph) < sourceIndex or len(self.graph) < destIndex:
            print("Posições inválidas")
            return

        self.graph[sourceIndex][destIndex] = 0

        if not directed:
            self.graph[destIndex][sourceIndex] = 0

    def setWeight(self, sourceIndex, destIndex, weight):
        if len(self.graph) < sourceIndex or len(self.graph) < destIndex:
            print("Posições inválidas")
            return

        self.graph[sourceIndex][destIndex] = weight

    def removeNode(self, index):
        self.nodes.pop(index)

        self.graph.pop(index)

        for row in self.graph:
            row.pop(index)

    def getNode(self, index):
        return self.nodes[index]

    def printGraph(self):
        for row in self.graph:
            for weight in row:
                print(f" {weight} ", end='')
            print()

        print(self.nodes)

    def getAdjacentNodes(self, nodeIdx):
        if nodeIdx >= len(self.nodes):
            print("Nó invalido")
            return []

        adjacentNodes = []

        for i, weight in enumerate(self.graph[nodeIdx]):
            if weight > 0:
                adjacentNodes.append((i, weight))

        return adjacentNodes

    def getDijkstraPath(self, source, dest):
        if source >= len(self.nodes):
            print("Nó source invalido")
        if dest >= len(self.nodes):
            print("Nó de destino inválido")

        nodeIdx = source

        previousNodes = [ None for _ in range(len(self.nodes)) ]
        pathWeights = [ 1e1000 for _ in range(len(self.nodes)) ]
        pathWeights[nodeIdx] = 0

        isClosed = [ False for _ in range(len(self.nodes)) ]
        isClosed[nodeIdx] = True

        nodes = PriorityQueue()

        for i, weight in self.getAdjacentNodes(nodeIdx):
            if isClosed[i] == False and pathWeights[i] > weight + pathWeights[nodeIdx]:
                nodes.put((weight, i))
                pathWeights[i] = weight + pathWeights[nodeIdx]
                previousNodes[i] = nodeIdx


        while not nodes.empty():
            _, nodeIdx = nodes.get()

            if isClosed[nodeIdx]:
                continue

            isClosed[nodeIdx] = True

            for i, weight in self.getAdjacentNodes(nodeIdx):
                if isClosed[i] == False and pathWeights[i] > weight + pathWeights[nodeIdx]:
                    nodes.put((weight, i))
                    pathWeights[i] = weight + pathWeights[nodeIdx]
                    previousNodes[i] = nodeIdx

        path = []
        path.append(dest)
        previousNode = previousNodes[dest]

        while previousNode != None:
            path.append(previousNode)
            previousNode = previousNodes[previousNode]

        path.reverse()

        return path

    def find_parent(self, parents, node):
        if parents[node] == node:
            return node
        return self.find_parent(parents, parents[node])


    def kruskal(self):
        #ordenr as arestas
        mst = []
        paths = []

        # PESO SOURCE DEST
        for i in range(len(self.nodes)):
            for j in range(i, len(self.nodes)):
                weight = self.graph[i][j]
                if weight > 0:
                    paths.append((weight, self.nodes[i], self.nodes[j]))

        paths.sort(key=lambda x: x[0])

        #lista de "pais"
        parents ={ node: node for node in range(len(self.nodes))}

        for path in paths:
            weight, source, dest = path

            source_parent = self.find_parent(parents, self.nodes.index(source))
            dest_parent = self.find_parent(parents, self.nodes.index(dest))

            if source_parent != dest_parent:
                mst.append((source, dest))
                parents[source_parent] = dest_parent

        return mst

    def __str__(self):
        return tabulate(self.graph, headers=self.nodes, showindex=self.nodes, numalign="center", tablefmt='orgtbl')


if __name__ == '__main__':
    g = Graph()
    g.insertNode("A") # 0
    g.insertNode("B") # 1
    g.insertNode("C") # 2
    g.insertNode("D") # 3
    g.insertNode("E") # 4
    g.insertNode("F") # 5
    g.insertNode("G") # 6

    g.insertPath(0, 1, 2, False)
    g.insertPath(0, 3, 3, False)
    g.insertPath(0, 2, 3, False)
    g.insertPath(1, 2, 4, False)
    g.insertPath(1, 4, 3, False)
    g.insertPath(2, 3, 5, False)
    g.insertPath(2, 4, 1, False)
    g.insertPath(3, 5, 7, False)
    g.insertPath(4, 5, 8, False)
    g.insertPath(5, 6, 9, False)

    mst = g.kruskal()
    print(mst)
