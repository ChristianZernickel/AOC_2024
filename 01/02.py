file = open("input.txt", "r")
lines = file.readlines()

a = []
b = {}

for line in lines:
    splitLine = line.split("   ")
    a.append(int(splitLine[0]))
    bLine = int(splitLine[1])
    if bLine not in b:
        b[bLine] = 1
    else:
        b[bLine] += 1

result = 0
for aValue in a:
    if aValue in b:
        result += (aValue * b[aValue])

print(result)