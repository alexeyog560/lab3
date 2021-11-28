import matplotlib.pyplot as plt
import math

a = []
b = []
text =[]
x=[]
y=[]

file = open("DS2.txt")
with file as f:
    for line in f:
            text.append([int(x) for x in line.split()])

for i in range(len(text)):
    for j in range(1):
        a.append(text[i][0])
        b.append(960 - text[i][1])
        a[i] -= 480
        b[i] -= 480
        x.append(int(a[i]) * math.cos(math.radians(30)) - int(b[i]) * math.sin(math.radians(30)))
        y.append(int(a[i]) * math.sin(math.radians(30)) + int(b[i]) * math.cos(math.radians(30)))
        x[i] += 480
        y[i] += 480
        a[i] += 480
        b[i] += 480

plt.scatter(x, y)
plt.show()
plt.close()
file.close()
