#3D Scatter Plot

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

readFile = open('/home/andrew/Downloads/2007_truncated.csv', 'r')
sepFile = readFile.readlines()
readFile.close()

X = []
Y = []
Z = []

for plotPair in sepFile:
    xAndY = plotPair.split(',')
    X.append(int(xAndY[1]))
    Y.append(int(xAndY[14]))
    Z.append(int(xAndY[3]))

ax.plot_wireframe(X,Y,Z, rstride=1, cstride=1)

ax.set_xlabel('Month')
ax.set_ylabel('Arrival Delay')
ax.set_zlabel('Day of the Week')

plt.show()

#There are 1311827 lines total!
