#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 01, 2022
#This program takes a users name and converts it to a different format. It also produces the users email.

fullName = input("Enter name in format firstName lastName: ")
names = fullName.split(" ")
print("name in LASTNAME, firstName format: " + names[1].upper() + ", " + names[0])

username = input("Enter user name of email: ")
print("email: " + username.lower() + "@hunter.cuny.edu")