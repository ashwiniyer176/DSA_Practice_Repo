myList = list()
listLength = int(input("Enter no of elements"))
for i in range(listLength):
    myList.append(int(input("Enter element")))
print(myList)
low = 0
high = listLength-1


def swap(v1, v2):
    temp = v1
    v1 = v2
    v2 = temp
    return v1, v2


while(low <= high):
    if(myList[low] < 0):
        low += 1
    else:
        myList[low], myList[high] = swap(myList[low], myList[high])
        high -= 1
        # low -= 1
print(myList)
