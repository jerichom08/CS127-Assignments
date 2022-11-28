#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 06, 2022
#This program takes user input of a phrase and prints out each letter,
#ASCII code of each letter, and the next two letter in the ASCII table.

phrase = input("Enter a phrase: ")
print("letter ASCII next_two_letter")

for i in phrase:
    print((i, ord(i), chr(ord(i) + 2)))