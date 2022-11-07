#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 27, 2022
#This program asks the user for a choice and saves a cropped image.

import matplotlib.pyplot as plt
import numpy as np

print('Enter 1 to get upper right corner\nEnter 2 to get midde portion')
num = int(input('Your choice: '))

if(num == 1):
    fileIn = input('Enter input file name: ')
    img = plt.imread(fileIn)
    height = img.shape[0]
    width = img.shape[1]
    newImg = img[:height//2, width//2:]
    fileOut = input('Enter output file name: ')
    plt.imsave(fileOut, newImg)
elif(num == 2):
    fileIn = input('Enter input file name: ')
    img = plt.imread(fileIn)
    height = img.shape[0]
    width = img.shape[1]
    height2 = int(height * 0.75)
    width2 = int(width * 0.75)
    newImg = img[height//4:height2, width//4:width2]
    fileOut = input('Enter output file name: ')
    plt.imsave(fileOut, newImg)
else:
    print('wrong choice')