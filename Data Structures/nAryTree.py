from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def printNode(self):
        print("Current Node:", self.data, "\nChildren:")
        for node in self.children:
            print(node.data)


class Tree:
    def __init__(self, rootNode):
        self.rootNode = rootNode

    def printTree(self, currentNode):
        if(len(currentNode.children) == 0):
            currentNode.printNode()
            return
        else:
            currentNode.printNode()
            for childNode in currentNode.children:
                self.printTree(childNode)

    def addNewNode(self, currentNode, newNode, queue):
        if(len(currentNode.children) <= 3):
            print("Adding to", currentNode.data)
            currentNode.children.append(newNode)
            return
        else:
            queue.extend(currentNode.children)
            nextNode = queue.pop(0)
            self.addNewNode(nextNode, newNode, queue)


rootNode = Node(0)
tree = Tree(rootNode)
prevNode = rootNode
for i in range(1, 10):
    nodeData = i
    tree.addNewNode(rootNode, Node(nodeData), [])
tree.printTree(tree.rootNode)
