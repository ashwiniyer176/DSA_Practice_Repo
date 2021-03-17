myList = list()
listLength = int(input("Enter Length of Array: "))
for i in range(0, listLength):
    x = int(input('Enter array element '))
    myList.append(x)
print(myList)
i = 0
# We are swapping every variable with its symmetrical oppsite in the array
while(i <= listLength-i-1):
    temp = myList[i]
    myList[i] = myList[listLength-i-1]
    myList[listLength-i-1] = temp
    i = i+1

print(myList)
