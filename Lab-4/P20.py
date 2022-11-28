#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 15, 2022
#This program modifies the NYC flood map from Lab 4 to color regions above 6 feet and less than or equal to 20 feet to the color gray. It also replaces red with yellow

import matplotlib.pyplot as plt
import numpy as np

elevations = np.loadtxt('elevationsNYC.txt')

plt.imshow(elevations)
plt.show()

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row, col] <= 0:
            floodMap[row, col, 2] = 1
        elif elevations[row, col] <= 6:
            floodMap[row, col, 0] = 1
            floodMap[row, col, 1] = 1
        elif elevations[row, col] <= 20:
            floodMap[row, col, 0] = 0.5
            floodMap[row, col, 1] = 0.5
            floodMap[row, col, 2] = 0.5
        else:
            floodMap[row, col, 1] = 1

plt.imshow(floodMap)
plt.show()

#plt.imsave('floodMap.png', floodMap)