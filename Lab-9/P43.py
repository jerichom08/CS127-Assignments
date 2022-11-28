#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 07, 2022
#This program creates a map of after school programs based on user input of a region or group.

import folium as fl
import pandas as pd

programs = pd.read_csv('after_school.csv')
mapPrograms = fl.Map(location=[40.75, -74.125], zoom_start=10)

choice = int(input('Enter 1 for Borough/Community,\n'
                   '2 for Grade Level / Age Group\n'
                   'Your choice: '))
if(choice == 1):
    mygroup = programs.groupby('Borough/Community')
    print(mygroup.groups.keys())
    groupName = input('Enter Borough/Community name: ')
    groupedData = mygroup.get_group(groupName)
    for i, r in groupedData.iterrows():
        lat = r['Latitude']
        lon = r['Longitude']
        name = r['Name']
        newMarker = fl.Marker([lat, lon], popup = name)
        newMarker.add_to(mapPrograms)
    newName = groupName.replace(' ', '_').lower()
    mapPrograms.save(outfile = newName + '_after_school.html')
elif(choice == 2):
    mygroup = programs.groupby('Grade Level / Age Group')
    print(mygroup.groups.keys())
    groupName = input('Enter Grade Level / Agre Group name: ')
    groupedData = mygroup.get_group(groupName)
    for i, r in groupedData.iterrows():
        lat = r['Latitude']
        lon = r['Longitude']
        name = r['Name']
        newMarker = fl.Marker([lat, lon], popup = name)
        newMarker.add_to(mapPrograms)
    newName = groupName.replace(' ', '_').replace('/', '_').lower()
    mapPrograms.save(outfile = newName + '_after_school.html')
