#3D Scatter Plot

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

readFile = open('/home/andrew/Downloads/2007_truncated.csv', 'r')
sepFile = readFile.readlines()
readFile.close()

rect = fig.patch
rect.set_facecolor('white')

X = []
Y = []
Z = []

for plotPair in sepFile:
    xAndY = plotPair.split(',')
    X.append(int(xAndY[20]))
    Y.append(int(xAndY[19]))
    Z.append(int(xAndY[4]))

ax.scatter(X,Y,Z, c ='r', marker='o')

ax.set_xlabel('TaxiOut Distance')
ax.set_ylabel('TaxiIn Distance')
ax.set_zlabel('Departure Time [GMT]')

plt.show()

#There are 1311827 lines total!
