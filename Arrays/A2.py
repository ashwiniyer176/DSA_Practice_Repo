myList = list()
listLength = int(input("Enter number of elements"))
head, tail = 0, listLength-1
for i in range(0, listLength):
    myList.append(int(input("Enter element:")))
big = myList[0]
small = myList[0]
print(myList)
for i in myList:
    if(big < i):
        big = i
    if(small > i):
        small = i

print(big, "\n", small)
