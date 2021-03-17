# Create a Graph and Print It. Nodes can be text or integers
from collections import defaultdict


class Graph:
    # If no data structure is specified, the graph stores the values in the form of a list
    graph = defaultdict(list)

    def addEdge(self, node1, node2):
        self.graph[node1].append(node2)

    def makeGraph(self, numberOfNodes):

        # Takes a node name and all the routes connected to the node
        # Thus, it can be a directed/undirected graph in the same code
        for i in range(numberOfNodes):
            sourceNode = input("Enter current node name:")
            edge = ""
            while(edge != "0"):
                edge = input(f"Enter node connected to {sourceNode}:")
                if(edge != "0"):
                    self.addEdge(sourceNode, edge)
        print(self.graph)


g = Graph()
numberOfNodes = int(input("Enter number of nodes: "))
g.makeGraph(numberOfNodes)
