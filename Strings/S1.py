import string

text = "Is this the real life, is this just fantasy?"
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print(reversed_text)
