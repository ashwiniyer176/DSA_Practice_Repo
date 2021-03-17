from collections import defaultdict
g = defaultdict(list)
g2 = defaultdict(list)
g[8] = ["g", "b"]
g2[8] = ["a", "b"]
# print(len(g.keys()))
# print(len(g.values()))

for key in g:
    print(key, g[key])


def checkIntersection():
    for key in g:
        if g2[key] != []:
            s1 = set(g[key])
            s2 = set(g2[key])
            intersected = len(s1.intersection(s2))
            interNode = list(s1.intersection(s2))
            if(intersected > 0):
                print("Intersecting", interNode)
            else:
                ("Not intersecting")
            print(s1, s2)


checkIntersection()
print(g)
