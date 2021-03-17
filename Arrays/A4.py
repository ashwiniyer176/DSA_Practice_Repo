myList = list()
listLength = int(input("Enter no of elements"))
for i in range(listLength):
    myList.append(int(input("Enter element")))
mid, i, beg = 0, 0, 0
end = listLength-1


def swap(v1, v2):
    temp = v1
    v1 = v2
    v2 = temp
    return v1, v2


while(mid <= end):
    print(myList)
    print(beg, mid, end)
    if(myList[mid] == 0):
        myList[beg], myList[mid] = swap(myList[beg], myList[mid])
        beg += 1
        mid += 1

    elif(myList[mid] == 1):
        mid += 1

    elif(myList[mid] == 2):
        myList[end], myList[mid] = swap(myList[end], myList[mid])
        mid -= 1
        end -= 1
    print('After itern')
    print(myList)
    print(beg, mid, end)
print(myList)
