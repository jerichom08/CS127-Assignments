#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 08, 2022
#This program takes an image and copies the image without the red channel.

import matplotlib.pyplot as plt
import numpy as np

imgName = input("Enter name of the input file: ")
img2Name = input("Enter name of the output file: ")
img = plt.imread(imgName)

img2 = img.copy()
img2[:, :, 0] = 0

plt.imsave(img2Name, img2)