from collections import defaultdict


class Node:
    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def printNode(self):
        print(self.data)


class Tree:
    def __init__(self, rootNode):
        self.rootNode = rootNode

    def printTree(self, currentNode):
        if(currentNode == None):
            return
        else:
            currentNode.printNode()
            self.printTree(currentNode.leftChild)
            self.printTree(currentNode.rightChild)
            return

    def addNewNode(self, currentNode, newNode, queue):
        if(currentNode.leftChild == None):
            currentNode.leftChild = newNode
            return
        elif(currentNode.rightChild == None):
            currentNode.rightChild = newNode
            return
        else:
            queue.extend([currentNode.leftChild, currentNode.rightChild])
            nextNode = queue.pop(0)
            self.addNewNode(nextNode, newNode, queue)


rootNode = Node(0)
tree = Tree(rootNode)
prevNode = rootNode
for i in range(1, 9):
    nodeData = i
    tree.addNewNode(rootNode, Node(nodeData), [])
tree.printTree(tree.rootNode)
