#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 07, 2022
#This program takes user input of the most popular neighborhoods in movies and movie directors in NYC based on the movie locations csv file.

import pandas as pd

locations = pd.read_csv('movie_locations.csv')
num1 = int(input('order of most popular neighborhoods in movies: '))
num2 = int(input('order of directors/filmmakers making most movies in NYC: '))
print(locations['Neighborhood'].value_counts()[:num1])
print(locations['Director/Filmmaker Name'].value_counts()[:num2])