file = open("input.txt", "r")
lines = file.readlines()

a = []
b = []

for line in lines:
    splitLine = line.split("   ")
    a.append(int(splitLine[0]))
    b.append(int(splitLine[1]))

a.sort()
b.sort()

result = 0

i = 0
for i in range(len(lines)):
    result += abs(a[i]-b[i])
    i += 1

print(result)