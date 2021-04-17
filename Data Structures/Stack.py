class stackElement:
    value = 0

    def updateElementValue(self, newValue):
        self.value = newValue


class Stack:
    stack = []
    top = -1

    def pushToStack(self, newValue):
        newElement = stackElement()
        newElement.updateElementValue(newValue)
        self.top += 1
        self.stack.append(newElement)

    def printStack(self):
        for i in self.stack:
            print(i.value, end=" ")
        print()


myStack = Stack()
for i in range(4):
    myStack.pushToStack(i)
    myStack.printStack()
