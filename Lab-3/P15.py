#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 12, 2022
#This program takes a phrase and prints out one less word each time. Then, it prints out one more word until the original phrase is back.

phrase = input("Enter a phrase: ")
words = phrase.split(' ')
for i in range(words.__len__(), 0, -1):
    print(' '.join(words[:i]))
for i in range(2, words.__len__() + 1):
    print(' '.join(words[:i]))