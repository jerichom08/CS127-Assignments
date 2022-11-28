#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 19, 2022
#This program takes user input of a file name and threshold, then calculates the number and percentage of white pixels in the image.

import matplotlib.pyplot as plt
import numpy as np

filename = input('Enter file name:')
t = float(input('Enter threshold: '))

img = plt.imread(filename)
plt.imshow(img)
plt.show()
snowCount = 0
totalCount = 0

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i, j, 0] > t and img[i, j, 1] > t and img[i, j, 2] > t):
            snowCount += 1
        totalCount += 1

print('number of white pixels: ' + str(snowCount))
print('percent of white pixels ' + str(round((snowCount/totalCount) * 100, 2)))