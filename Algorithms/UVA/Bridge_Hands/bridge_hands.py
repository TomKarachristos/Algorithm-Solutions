import os
import operator

file = open("input.txt", "r")

dealer = file.read(1)
file.read(1)
decks = {
    "N": ([], 'E'),
    "E": ([], "S"), 
    "S": ([], "W"),
    "W": ([], "N")
}

next_player = dealer
for i in range(52):
    if(i == 26):
        file.read(1)
    card = file.read(2)
    next_player = decks[next_player][1]
    decks[next_player][0].append(card)
    
deck_order = ['C', 'D', 'S', 'H', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
def custom_key(current_card):
   player_deck = []
   for order in current_card:
      player_deck.append(deck_order.index(order))
   return player_deck
 
N_deck = decks['N'][0].sort(key=custom_key)
E_deck = decks['E'][0].sort(key=custom_key)
S_deck = decks['S'][0].sort(key=custom_key)
W_deck = decks['W'][0].sort(key=custom_key)

print("S:", end=" ")
for index,card in enumerate(decks['S'][0]):
    if(index == 12):
        print(card)
    else:
        print(card, end= " ")

print("W:", end=" ")
for index,card in enumerate(decks['W'][0]):
    if(index == 12):
        print(card)
    else:
        print(card, end= " ")

print("N:", end=" ")
for index,card in enumerate(decks['N'][0]):
    if(index == 12):
        print(card)
    else:
        print(card, end= " ")

print("E:", end=" ")
for index,card in enumerate(decks['E'][0]):
    if(index == 12):
        print(card)
    else:
        print(card, end= " ")