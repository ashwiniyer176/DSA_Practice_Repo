from typing import NewType


class Node:
    def __init__(self, nodeName):
        self.nodeName = nodeName
        self.nextNode = None


class LinkedList:
    headNode = None
    tailNode = None

    def addNewNode(self):
        nodeName = input("Enter node name:")
        newNode = Node(nodeName)
        if(self.headNode == None):
            self.headNode = newNode
            self.tailNode = newNode
        elif(self.headNode.nextNode == None):
            self.headNode.nextNode = newNode
            self.tailNode = newNode
        else:
            self.tailNode.nextNode = newNode
            self.tailNode = newNode

    def printList(self):
        currentNode = self.headNode
        while(currentNode != None):
            print(currentNode.nodeName)
            currentNode = currentNode.nextNode


linkedlist = LinkedList()
for i in range(3):
    linkedlist.addNewNode()

linkedlist.printList()
