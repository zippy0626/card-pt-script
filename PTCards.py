from deck import Deck
import random
import sys

def getRandomCards(deck):
  if (len(deck) == 1):
    return 1
  else:
    return random.randrange(1, len(deck))

def checkUserOption(option, deck):
  # lambda is an anon function waiting to be executed
  options_map = {
    "r": getRandomCards(deck),
    "q": lambda: sys.exit()
  }
  if (option in options_map):
    if (option == "r"): return options_map[option]
    else: return options_map[option]()
  else:
    return int(option)

deck = Deck()

print("\nCards PT\n\nHearts = Squats\nSpades = Push Ups\nClubs = Russian Twists\nDiamonds = Burpees")
print('''
Ace = 14 reps
King = 13 reps
Queen = 12 reps
Jack = 11 reps

eg. Jack of Diamonds = 11 burpees    
''')

cardsToDraw = None
usrOption = None
timesDrew = 0
plankTimeSeconds = 0

## loop
while True:
  if (len(deck) == 0):
    print("\nYou finished Card PT!\n")
    sys.exit()
  
  if (timesDrew >= 1):
    usrOption = input(" Continue? Enter number of cards to draw, 'r' for random, 'q' to quit: ")
    print("\n")
  else:
    usrOption = input(" Enter number of cards to draw, 'r' for random, 'q' to quit: ")
    print("\n")
  
  try:
    cardsToDraw = checkUserOption(usrOption, deck)
    if (cardsToDraw < 1 or cardsToDraw > len(deck)):
      print(f"Invalid Input. Please enter a number between 1 and {len(deck)}.\n")
      continue
  except ValueError:
    print("Invalid input. Please enter a number, 'r' for random, 'q' to quit.\n")
    continue
  
  timesDrew += 1
  
  for i in range(cardsToDraw):
    card = deck.draw()
    [amount, exercise] = card.getExercise()
    print(f"{card}: {amount} {exercise}, {amount * 3} sec plank")
    plankTimeSeconds += (amount * 3)

  deck.printCardsRemaining()
  print(f"{plankTimeSeconds // 60}:{plankTimeSeconds % 60:02d} min total plank")