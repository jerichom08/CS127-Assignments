#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 24, 2022
#This program uses the function main() to count the number of letters in a string.

def main():
    string = input('Enter a string: ')
    ch = input('Enter a char: ')
    print('number of \'' + ch + '\' in \"' + string + '\" is ' + str(string.count(ch)))
    
main()