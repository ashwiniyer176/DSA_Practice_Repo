l1 = list()
l2 = list()

len1 = int(input("Enter Length of Array 1: "))
for i in range(0, len1):
    l1.append(int(input('Enter array element ')))

len2 = int(input("Enter Length of Array 2: "))
for i in range(0, len2):
    l2.append(int(input('Enter array element ')))

print(len1)
print(len2)
big = len1+len2
small = abs(len1-len2)
i, j = 0, 0
# for union
print("Union:")
while (i < len1 and j < len2):
    if(l1[i] < l2[j]):
        print(l1[i], end=" ")
        i += 1
    elif(l1[i] > l2[j]):
        print(l2[j], end=" ")
        j += 1
    else:
        print(l2[j], end=" ")
        i += 1
        j += 1
while(i < len1):
    print(l1[i], end=" ")
    i += 1

while(j < len2):
    print(l2[j], end=" ")
    j += 1
i, j = 0, 0
print("")
print("Intersection:")
while (i < len1 and j < len2):
    if(l1[i] < l2[j]):
        i += 1
    elif(l1[i] > l2[j]):
        j += 1
    else:
        print(l2[j], end=" ")
        i += 1
        j += 1
