"""
probability by a roulette game from 400 tries one digit will not show up
"""

import random as random

def iteration():
    for _ in range(400):
        rand = random.randrange(0,37)
        # we chooose 10 the number not to apear
        if rand == 10:
            return True
    return False

def generate(retry):
    for _ in range(retry):
        numberExists = iteration()
        if not numberExists:
            print('number not exists')
            return
    print('number exists')

generate(10000)

print(1 - (36/37)**400)