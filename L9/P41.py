#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 07, 2022
#This program creates a map centered in NYC with a marker at central park.

import folium as f

mapNYC = f.Map(location = [40.75, -74.125], zoom_start = 10)
f.Marker(location = [40.7812, -73.9665], popup = 'Central Park').add_to(mapNYC)
mapNYC.save(outfile = 'nyc_Central_park.html')