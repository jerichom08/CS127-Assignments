#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 06, 2022
#This program takes user input of a string and int shifts the letters right by that int.

word = input("Enter an all-small-letter string: ")
num = int(input("Enter a non-neagative int to shift: "))

cipher = ""
for i in word:
    ascii = ord(i) + num
    if(ascii > 122):
        ascii -= 26
    cipher += chr(ascii)
print("ciphered string: " + cipher)