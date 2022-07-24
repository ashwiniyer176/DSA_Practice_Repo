text = "Is this the real life, is this just fantasy?"
occurences = {}
for i in text:
    try:
        occurences[i] += 1
    except KeyError:
        occurences[i] = 1
for i in occurences:
    if occurences[i] > 1:
        print(i)
