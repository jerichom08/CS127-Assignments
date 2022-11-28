#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 21, 2022
#This program has a function that makes sure the user enters an integer between 1 and 6. Then, the computer generates a random number between 1 and 6. The number and sum determines whether the user or computer wins.

import random

def userNum():
    num = int(input('Enter only 1-6: '))
    while(num < 1 or num > 6):
        print('Input needs to be in 1-6. Re-enter:')
        num = int(input('Enter only 1-6: '))
    return num
        
def compareNum():
    user = userNum()
    print('user: ' + str(user))
    computer = random.randrange(1, 7)
    print('computer: ' + str(computer))
    if(user == computer):
        print('draw')
    elif(user + computer == 3 or user + computer == 6 or user + computer == 7 or user + computer == 8):
        print('user wins')
    else:
        print('computer wins')

def main():
    compareNum()

if __name__ == '__main__':
    main()