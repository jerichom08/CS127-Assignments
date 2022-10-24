#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 15, 2022
#This program allows the user to choose a conversion and enter values to convert.

print('(a) convert centimeters to feet\n(b) convert centimeters to feet and inches\n(c) convert feet and inches to centimeters')

choice = input('Enter a or b or c: ')
if(choice == 'a'):
    cm = int(input('Enter height in centimeters: '))
    feet = round(cm/30.48, 2)
    print('height is', feet,'feet')

elif(choice == 'b'):
    cm = int(input('Enter height in centimeters: '))
    feet = int(cm/30.48)
    inches = int((cm - feet * 30.48)/2.54)
    if(inches == 0):
        print('height is', feet,'feet')
    else:
        print('height is', feet,'feet and', inches,'inches')

elif(choice == 'c'):
    feet_str, inches_str = input('Enter height in feet and inches, separated by a space: ').split()
    feet = int(feet_str)
    inches = int(inches_str)
    inches += feet * 12
    cm = round(inches * 2.54)
    print('height is', cm,'cm')

else:
    print('Wrong choice, please enter only a or b or c')