# NOMES: Pedro Porto, Gabriel Bessa

from tabulate import tabulate

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

    def __str__(self):
        return tabulate(self.graph, headers=self.nodes, showindex=self.nodes, numalign="center", tablefmt='orgtbl')
    
if __name__ == '__main__':
    g = Graph()
    g.insertNode("pelotas")
    g.insertNode("canguçu")
    g.insertPath(0, 1, 5, False)
    # g.printGraph()
    print(g)
