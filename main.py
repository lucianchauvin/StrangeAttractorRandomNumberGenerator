import time
import math
from matplotlib import pyplot as plt


def lorenze(x):
    y = 1
    z = 1
    for i in range(round(10000*x)):
        xdot = 10*(y-x)
        ydot = 28*x-y-x*z
        zdot = x*y - (8/3)*z

        x += xdot*.005
        y += ydot*.005
        z += zdot*.005

    out = abs(x)
    digBeforeDec = str(out).index(".")
    return out/10**(digBeforeDec-1)

# plotting data


data = []

for i in range(10000):
    milliseconds = int(round(time.time() * 1000))
    normalized = milliseconds/1000000000000
    data.append(round(lorenze(normalized)))

amounts = []
for x in range(11):
    amounts.append(data.count(x))

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.bar(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], amounts)
plt.show()
