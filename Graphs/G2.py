# BFS in an Undirected Graph
from collections import defaultdict


class Graph:
    # If no data structure is specified, the graph stores the values in the form of a list
    graph = defaultdict(list)
    visitedNodes = list()
    queue = list()

    def addEdge(self, node1, node2):
        # Since there is no limit on direction, it makes sense that if A is connected to B, B will be connected to A
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def makeGraph(self, numberOfNodes):

        # Takes a node name and all the routes connected to the node
        for i in range(numberOfNodes):
            sourceNode = input("Enter current node name:")
            edge = ""
            while(edge != "0"):
                edge = input(f"Enter node connected to {sourceNode}:")
                if(edge != "0"):
                    self.addEdge(sourceNode, edge)
        print(self.graph)

    def breadthFirstSearch(self, sourceNode, key):
        print(self.visitedNodes, "\n", self.queue)
        if(len(self.visitedNodes) != 0 and len(self.queue) == 0):
            print(sourceNode)
            self.visitedNodes.append(sourceNode)
            print(self.visitedNodes, "\n", self.queue)
            return

        if(key == sourceNode):
            self.visitedNodes.append(sourceNode)
            return

        else:
            print(sourceNode)
            self.visitedNodes.append(sourceNode)

            for node in self.graph[sourceNode]:
                if node not in self.visitedNodes and node not in self.queue:
                    self.queue.append(node)

            nextNode = self.queue.pop(0)
            self.breadthFirstSearch(nextNode, key)
            return


g = Graph()
numberOfNodes = int(input("Enter number of nodes: "))
g.makeGraph(numberOfNodes)
sourceNode = input("Enter Source Node:")
key = input("Enter key: ")
g.breadthFirstSearch(sourceNode, key)

if(g.visitedNodes[-1] == key):
    print("Key Found")
else:
    print("Not found")
