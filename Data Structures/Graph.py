from collections import defaultdict


class Graph:
    graph = defaultdict(list)

    def addEdge(self, node1, node2):
        self.graph[node1].append(node2)

    def makeGraph(self, numberOfNodes):
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
