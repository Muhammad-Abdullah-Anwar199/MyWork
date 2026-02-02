#from random import choice
import random
'''coin = random.choice(["heads" , "tails"])
print(coin)'''

'''number = random.randint(1,10)
print(number)'''

cards = ["jack" , "king" , "queen"]
random.shuffle(cards)
for index , card in enumerate(cards):
    print(index , card , sep=". ")