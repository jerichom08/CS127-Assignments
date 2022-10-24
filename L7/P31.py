#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 20, 2022
#This program creates a plot based on the country_internet.csv file and saves it to a file name entered by the user.

import matplotlib.pyplot as plt
import pandas as pd


internet = pd.read_csv('country_internet.csv')
internet['Percentage'] = (internet['Internet users']/internet['Population']) * 100
internet.plot(x = 'Country', y = 'Percentage')

filename = input('Enter output file name: ')
fig = plt.gcf()
fig.savefig(filename)