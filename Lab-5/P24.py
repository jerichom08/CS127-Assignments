#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: October 03, 2022
#This program takes user input of a list of words and returns the number of words ending with an 'a' or 'b' and the fraction of words ending with those letters.

list = input('Enter a list of words, separated by a space: ')
words = list.split(' ')
abwords = 0
for i in words:
    if(i[-1] == 'a' or i[-1] == 'b'):
        abwords += 1
print('number of words: ' + str(words.__len__()))
print('number of words ending with a or b: ' + str(abwords))
print('fraction of words ending with a or b: ' + str(round(abwords/words.__len__(), 2)))