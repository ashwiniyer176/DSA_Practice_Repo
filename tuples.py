l = [("a", 11), ("b", 2), ("c", 3)]
print(l)
small = l[0]
for node in l:
    if(node[-1] < small[-1]):
        small = node
l.remove(small)

print(l)
