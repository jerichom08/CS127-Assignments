#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: September 08, 2022
#This program takse user input of a phrase and reverses it, reverses it in uppercase, and abbreviates it.

phrase = input("input: ")
reverse = ""

for i in range(len(phrase) - 1, -1, -1):
    reverse += phrase[i]
print("user reverse: " + reverse)
print("user reverse upper: " + reverse.upper())

words = phrase.split(' ')
acronym = ""
for word in words:
    acronym += word[0].upper()
print("user abbreviation: " + acronym)