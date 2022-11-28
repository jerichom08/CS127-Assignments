#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 20, 2022
#This program allows the user to retrieve data from children_lead.csv that is grouped by borough or year.

import matplotlib.pyplot as plt
import pandas as pd

lead = pd.read_csv('children_lead.csv')

choice = input('Enter a choice:\na. group by borough\nb. group by year\n')
if(choice == 'a'):
    print('average number of affected children by borough')
    groupedData = lead.groupby('borough')
    print(groupedData['affected_children'].mean())
    
    borough = input('Enter a borough: ')
    boroughData = groupedData.get_group(borough)
    print('average number of affected children of ' + borough + ' is ' + str(boroughData['affected_children'].mean()))
    print('min number of affected children of ' + borough + ' is ' + str(boroughData['affected_children'].min()))
    print('max number of affected children of ' + borough + ' is ' + str(boroughData['affected_children'].max()))
elif(choice == 'b'):
    print('average number of affected children by year')
    groupedData = lead.groupby('year')
    print(groupedData['affected_children'].mean())
    
    year = int(input('Enter a year (2005 - 2016): '))
    yearData = groupedData.get_group(year)
    print('average number of affected children in ' + str(year) + ' is ' + str(yearData['affected_children'].mean()))
    print('min number of affected children in ' + str(year) + ' is ' + str(yearData['affected_children'].min()))
    print('max number of affected children in ' + str(year) + ' is ' + str(yearData['affected_children'].max()))
else:
    print('wrong choice')