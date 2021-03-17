# Best First Search in an Undirected Graph
from collections import defaultdict
import math


class Graph:
    graph = defaultdict(list)
    visitedNodes = []
    heuristicValues = defaultdict(float)
    nodeCoordinates = defaultdict(tuple)
    rootNode = ""
    path = []
    pathList = defaultdict(list)
    intersectingNodes = []
    reversePathList = defaultdict(list)

    def BidirectionalSearch(self, sourceNode, targetNode, numberOfNodes):
        print("Forward Traversal")
        for i in range(numberOfNodes-2):
            self.rootNode = sourceNode
            self.calculateHeuristicValues(targetNode)
            costOfPath = self.BestFirstSearch(sourceNode, targetNode, 0)
            self.pathList[costOfPath] = self.path
            self.path = []
        print("Forward Paths:", self.pathList)

        print("Reverse Traversal")
        for i in range(numberOfNodes-2):
            self.rootNode = targetNode
            self.calculateHeuristicValues(sourceNode)
            costOfPath = self.BestFirstSearch(targetNode, sourceNode, 0)
            self.reversePathList[costOfPath] = self.path
            self.path = []
        print("Reverse Paths: ", self.reversePathList)

        if(self.checkIntersection()):
            print("Intersecting at: ", self.intersectingNodes)
        else:
            print("Not Intersecting")

    def checkIntersection(self):
        for key in self.pathList:
            if self.reversePathList[key] != []:
                s1 = set(self.pathList[key])
                s2 = set(self.reversePathList[key])
                intersection = len(s1.intersection(s2))
                self.intersectingNodes = list(s1.intersection(s2))
                if(intersection > 0):
                    return True
                else:
                    return False

    def getNodeCoordinates(self, numberOfNodes):
        for i in range(numberOfNodes):
            nodeName = input("Enter Node Name: ")
            xValue = int(input("Enter X Coordinate: "))
            yValue = int(input("Enter Y Coordinate: "))
            self.nodeCoordinates[nodeName] = (xValue, yValue)

    def BestFirstSearch(self, sourceNode, targetNode, currentCost):
        if(sourceNode == targetNode):
            return currentCost

        else:
            self.addToVisitedNodes(sourceNode)
            queue = self.graph[sourceNode]
            nextNode = self.findNextNode(queue)
            currentCost += nextNode[-1]
            self.path.append(sourceNode)
            return self.BestFirstSearch(nextNode[0], targetNode, currentCost)

    def addToVisitedNodes(self, node):
        if(node not in self.visitedNodes and node != self.rootNode):
            self.visitedNodes.append(node)

    def addEdge(self, node1, node2, cost):
        t1 = (node1, cost)
        t2 = (node2, cost)
        self.graph[node1].append(t2)
        self.graph[node2].append(t1)

    def getEuclideanDistance(self, t1, t2):
        x1 = t1[0]
        y1 = t1[1]
        x2 = t2[0]
        y2 = t2[1]
        distance = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)
        return distance

    def calculateHeuristicValues(self, targetNode):
        targetCoordinates = self.nodeCoordinates[targetNode]
        for node in self.nodeCoordinates:
            if(node == targetNode):
                self.heuristicValues[targetNode] = 0
            else:
                currentNodeCoordinates = self.nodeCoordinates[node]
                euclideanDistance = self.getEuclideanDistance(
                    targetCoordinates, currentNodeCoordinates)
                self.heuristicValues[node] = euclideanDistance

    def makeGraph(self, numberOfNodes):
        print("Enter Node Names and Edges associated with it. \nEnter '.' to stop adding edges to current node:\n")
        for i in range(numberOfNodes):
            sourceNode = input("Enter current node name:")
            edge = ""
            while(edge != "."):
                edge = input(f"Enter node connected to {sourceNode}:")
                if(edge != "."):
                    cost = int(input("Enter cost: "))
                    self.addEdge(sourceNode, edge, cost)
        print(self.graph)

    def findNextNode(self, queue):
        small = queue[0]
        for node in queue:
            if node[0] not in self.visitedNodes:
                if self.heuristicValues[node[0]] < self.heuristicValues[small[0]]:
                    small = node
        return small


g = Graph()
numberOfNodes = int(input("Enter number of Nodes: "))
sourceNode = input("Enter Source Node:")
targetNode = input("Enter Target Node:")

g.getNodeCoordinates(numberOfNodes)

g.makeGraph(numberOfNodes)

g.BidirectionalSearch(sourceNode, targetNode, numberOfNodes)
