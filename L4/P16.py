#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 12, 2022
#This program takes user input of a list of names and converts it to show the first initial and last name.

names = input("Enter a list of names, separated by semicolon: ")
names = names.split(';')

for i in names:
    name = i.split(' ')
    print(name[0][0] + '. ' + name[1])
