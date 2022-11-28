#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 06, 2022
#This program takes a binary string and converts it to a number.

string = input('Enter a string with 0 or 1 only: ')
num = 0;
base = 2;
weight = 1;
length = string.__len__()

for i in string[::-1]:
    ch = i
    if(ch == '1'):
        num += weight
    elif(ch != '0'):
        print('letter ' + ch + ' is not allowed in binary string.')
        exit()
    weight *= base
    
print('num = ' + str(num))