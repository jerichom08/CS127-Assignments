#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 03, 2022
#This program asks for an hour of the day and greets the user based on the hour.

hour = int(input('Enter hour (in 24 hour time): '))
if(hour < 12):
    print('Good Morning')
elif(hour >= 12 and hour < 17):
    print('Good Afternoon')
else:
    print('Good Evening')