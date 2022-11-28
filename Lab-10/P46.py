#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 17, 2022
#This program asks for a number and determines whether it is a perfect number.

def isPerfect(num):
    if(num <= 0):
        return False
    total = 0
    for i in range(1, num//2 + 1):
        if(num % i == 0):
            total += i
    if(total == num):
        return True
    else:
        return False

def main():
    num = int(input('Enter a perfect number: '))
    while(isPerfect(num) == False):
        num = int(input(str(num) + ' is not a perfect number. Re-enter: '))
    print('Congratulations! ' + str(num) + ' is a perfect number.')
    
if __name__ == "__main__":
    main()