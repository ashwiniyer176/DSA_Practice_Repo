# Detecting Cycle in an undirected graph with BFS
from collections import defaultdict


class Graph:
    # If no data structure is specified, the graph stores the values in the form of a list
    graph = defaultdict(list)
    visitedNodes = list()
    queue = list()
    numberOfEdges = 0
    numberOfNodes = 0

    def addEdge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    # Check: Is a cycle possible in the graph (using Minimum Spanning Tree property)?
    def verifyCyclic(self):
        numberOfEdges = self.numberOfEdges
        numberOfVertices = self.numberOfNodes
        print("Edges = ", numberOfEdges, "\nVertices = ", numberOfVertices)
        if(numberOfEdges >= numberOfVertices):
            return True
        return False

    def makeGraph(self, numberOfNodes):
        # Takes a node name and all the edges connected to the node. Also updates number of edges and vertices
        self.numberOfNodes = numberOfNodes
        for i in range(numberOfNodes):
            sourceNode = input("Enter current node name:")
            edge = ""
            while(edge != "."):
                edge = input(f"Enter node connected to {sourceNode}:")
                if(edge != "."):
                    self.addEdge(sourceNode, edge)
                    self.numberOfEdges += 1
        print(self.graph)

    def breadthFirstSearch(self, sourceNode):
        if(sourceNode in self.visitedNodes):
            return True
        else:
            print(sourceNode)
            self.visitedNodes.append(sourceNode)
            for node in self.graph[sourceNode]:
                if node not in self.queue:
                    self.queue.append(node)
            nextNode = self.queue.pop(0)
            flag = self.breadthFirstSearch(nextNode)
            return flag


g = Graph()
numberOfNodes = int(input("Enter number of nodes: "))
g.makeGraph(numberOfNodes)
sourceNode = input("Enter Source Node:")
if(g.verifyCyclic()):
    flag = g.breadthFirstSearch(sourceNode)

else:
    flag = False
print(flag)
