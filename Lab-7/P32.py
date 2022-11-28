#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 20, 2022
#This program prints out the average of the number of internet plans in each continental region. It also creates a bar plot of a selected region.

import matplotlib.pyplot as plt
import pandas as pd

internet = pd.read_csv('country_internet.csv')
groupedData = internet.groupby('Continental region')
print(groupedData['NO. OF Internet Plans'].mean())

print('possible regions are\n' + str(groupedData.groups.keys()))
region = input('choose a region: ')
regionData = groupedData.get_group(region)
print('number of countries: ' + str(regionData['NO. OF Internet Plans'].count()))
print('maximum number of internet plans: ' + str(regionData['NO. OF Internet Plans'].max()))
print('minimum number of internet plans: ' + str(regionData['NO. OF Internet Plans'].min()))

#output = input('PLease enter output file name: ')
regionData.plot.bar(x = 'Country', y = 'NO. OF Internet Plans')
plt.gcf().subplots_adjust(bottom = 0.25)
plt.xlabel('Country in ' + region)
plt.ylabel('NO. OF Internet Plans')
plt.show()
#fig = plt.gcf()
#fig.savefig(output)