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

    def prim(self, start = "A"):
        mst = {}
        visited = []
        queue = []
                    # peso, nó
        queue.append((0, start))

        while queue:
            queue.sort(key=lambda x: x[0])
            weight, current_node = queue.pop(0)

            if current_node in visited:
                continue

            visited.append(current_node)

            current_index = self.nodes.index(current_node)

            for connection_index, path_weight in enumerate(self.graph[current_index]):
                neighbor_node = self.nodes[connection_index]

                if path_weight > 0 and neighbor_node not in visited:
                    mst[neighbor_node] = current_node

                    queue.append((path_weight, neighbor_node))

        return mst

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

    def __str__(self):
        return tabulate(self.graph, headers=self.nodes, showindex=self.nodes, numalign="center", tablefmt='orgtbl')


if __name__ == '__main__':
    g = Graph()
    g.nodes = ['A', 'B', 'C', 'D']
    g.graph = [
        [0, 2, 1, 0],
        [2, 0, 3, 0],
        [1, 3, 0, 5],
        [0, 0, 5, 0]
    ]
    mst = g.prim("A")
    print(mst)
