#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 15, 2022
#This program creates a blue and green t-shape with a yellow background.

import matplotlib.image as img
import numpy as np

tshape = np.zeros([30, 30, 3])
tshape[:, :, 0] = 1
tshape[:, :, 1] = 1

for i in range(5, 8):
    for j in range(5, 25):
        tshape[i, j, 0] = 0
        tshape[i, j, 1] = 0
        tshape[i, j, 2] = 1

for i in range(8, 25):
    for j in range(13, 16):
        tshape[i, j, 0] = 0
        tshape[i, j, 1] = 1
        tshape[i, j, 2] = 0

imgname = input('Enter output file name: ')
img.imsave(imgname, tshape)
