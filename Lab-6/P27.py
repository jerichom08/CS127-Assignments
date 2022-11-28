#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 18, 2022
#This program displays statistics of a borough based on the daily covid cases csv file.

import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter a csv file: ")
borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
output = input("Enter output name: ")

cases = pd.read_csv(name)
print('Min: ' + str(cases[borough].min()))
print('Max: ' + str(cases[borough].max()))
print('Mean: ' + str(round(cases[borough].mean(), 3)))
print('Median: ' + str(cases[borough].median()))
print('Standard Deviation: ' + str(round(cases[borough].std(), 3)))

cases['Fraction'] = cases[borough]/cases['case_count']
cases.plot(x = 'date_of_interest', y = 'Fraction')

fig = plt.gcf()
fig.savefig(output)