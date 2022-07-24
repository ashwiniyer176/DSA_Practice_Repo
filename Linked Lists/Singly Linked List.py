class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def insertNode(self, node):
        x = self.head
        while x.next is not None:
            x = x.next
        x.next = node

    def deleteNode(self, val):
        x = self.head
        prev = None
        if x.val == val:
            self.head = self.head.next
        while x is not None:
            if x.val == val and prev is not None:
                prev.next = x.next
                break
            prev = x
            x = x.next
        self.printList()

    def printList(self):
        x = self.head
        while x is not None:
            print(x.val, end="->")
            x = x.next
        print()


if __name__ == "__main__":
    root = Node(0)
    first = Node(1)
    second = Node(2)
    ll = LinkedList(root)
    ll.insertNode(first)
    ll.insertNode(second)
    ll.printList()
    ll.deleteNode(1)
