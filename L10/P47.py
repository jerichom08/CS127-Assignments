#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 17, 2022
#This program guesses a random number picked by the user between 0 and 100.

start = 0
mid = 0
end = 100
guess = 1
choice = 0

print('Pick an integer in [0, 100] in your mind.')
num = 26
while(choice != 3):
    mid = int((start + end) // 2)
    print('Guess ' + str(guess) +': is it ' + str(mid) + '?')
    choice = int(input('Enter choice 1-3: '))
    if(choice == 1):
        start = mid + 1
    elif(choice == 2):
        end = mid - 1
    guess += 1
print('Congratulations! The answer is ' + str(mid))