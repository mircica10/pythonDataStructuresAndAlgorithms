"""
https://math.stackexchange.com/questions/1303497/what-is-the-algorithm-to-generate-the-cards-in-the-game-dobble-known-as-spo
"""

def dobble(n):
    cards = []
    for i in range(n):
        for j in range(n):
            cards.append([ ( (i*k + j) % n ) * n + k for k in range(n)] + [n*n + i])
    for i in range(n):
        cards.append([j * n + i for j in range(n)] + [n*n + n])
    cards.append([n * n + i for i in range(n+1)])
    return cards

from itertools import combinations
for card1, card2 in combinations(dobble(7),2):
    assert( len( set(card1) & set(card2) ) == 1 )

