#Name: Jericho Maniago
#Email: jericho.maniago49@myhunter.cuny.edu
#Date: November 06, 2022
#This program has a function that returns the price of a drink.

def computePrice(liquid, size):
    if(liquid == 'coffee'):
        if(size == 'small'):
            return 2.5
        elif(size == 'medium'):
            return 2.75
        elif(size == 'large'):
            return 3.00
        else:
            return -1
    elif(liquid == 'misto'):
        if(size == 'small'):
            return 3.15
        elif(size == 'medium'):
            return 3.35
        elif(size == 'large'):
            return 3.7
        else:
            return -1
    elif(liquid == 'mocha'):
        if(size == 'small'):
            return 3.5
        elif(size == 'medium'):
            return 3.8
        elif(size == 'large'):
            return 4.25
        else:
            return -1
    elif(liquid == 'tea'):
        if(size == 'small'):
            return 2.35
        elif(size == 'medium'):
            return 2.45
        elif(size == 'large'):
            return 2.90
        else:
            return -1
    else:
        return -1