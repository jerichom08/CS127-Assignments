#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 15, 2022
#This programs takes user input of an integer and creates that amount of green and blue stripes.

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

num = int(input('Enter the size: ')) + 1
stripes = np.zeros([num, num, 3])

for i in range(num):
    for j in range(num):
        if j % 2 == 0:
            stripes[i, j, 2] = 1
        else:
            stripes[i, j, 1] = 1

imgname = input('Enter output file: ')
img.imsave(imgname, stripes)