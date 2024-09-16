import random

def create_deck():
  suits = ["♥", "♦", "♣", "♠"]
  ranks =["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = [] 
  for suit in suits: 
    for rank in ranks: 
      deck.append((suit,rank))
  random.shuffle(deck)
  return deck

def draw_card(deck, quantity):
  hand = []
  for _ in range(quantity):
    if deck:
      hand.append(deck.pop())
  return hand, deck

deck = create_deck() 

def show_card(card):
    space = " "
    if len(card[1]) == 2:
        space = ""
    print (f"""
+-------+
|{card[1]}     {space}|
|       |
|   {card[0]}   |
|       |
|{space}     {card[1]}|
+-------+
""")

while deck:
  input("Press Enter to draw the next card")
  hand, deck = draw_card(deck, 1)
  for card in hand:
    show_card(card)  

print("We are out of cards")