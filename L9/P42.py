#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 07, 2022
#This program creates a map of NYC hospitals based on the NYC hospitals csv file.

import folium as fl
import pandas as pd

out = input('Enter output file: ')

hospitals = pd.read_csv('nyc_hospitals.csv')
mapHospitals = fl.Map(location=[40.75, -74.125], zoom_start=10)
for i, r in hospitals.iterrows():
    lat = r['Latitude']
    lon = r['Longitude']
    name = r['Facility Name']
    newMarker = fl.Marker([lat, lon], popup = name)
    newMarker.add_to(mapHospitals)

mapHospitals.save(outfile = out)