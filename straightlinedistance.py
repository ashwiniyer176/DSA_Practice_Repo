import math


def getEuclideanDistance(self, t1, t2):
    print(t1, t2)
    x1 = t1[0]
    y1 = t1[1]
    x2 = t2[0]
    y2 = t2[1]
    distance = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)
    print(distance)


getEuclideanDistance(0, (3, 4), (5, 6))
