from deck import Deck
import random
import sys

def getRandomCards(deck):
  if (len(deck) == 1):
    return 1
  else:
    return random.randrange(1, len(deck))

def checkUserOption(option):
  # lambda is an anon function waiting to be executed
  options_map = {
    "r": getRandomCards,
    "q": lambda: sys.exit()
  }
  if (option in options_map):
    if (option == "r"): return options_map[option](deck)
    else: return options_map[option]()
  else:
    return int(option)


## initial run
deck = Deck()

print("\nCards PT\n\nHearts = Squats\nSpades = Push Ups\nClubs = Russian Twists\nDiamonds = Burpies\n")
print('''Ace = 14 reps
King = 13 reps
Queen = 12 reps
Jack = 11 reps

eg. Jack of Diamonds = 11 burpees    
''')

option = input("Enter number of cards to draw, 'r' for random, 'q' to quit: ")
print()

number = checkUserOption(option)
for i in range(number):
  card = deck.draw()
  [amount, exercise] = card.getExercise()
  print(f"{card}: {amount} {exercise}, {amount * 3} sec plank")

deck.printCardsRemaining()
##


## loop
while True:
  if (len(deck) == 0):
    print("\nYou finished Card PT!\n")
    sys.exit()

  option = input("Continue? Enter number of cards to draw, 'r' for random, 'q' to quit: ")
  print()

  try:
    number = checkUserOption(option)
    if number < 1 or number > len(deck):
      print(f"  Invalid Input. Please enter a number between 1 and {len(deck)}.\n")
  except ValueError:
    print(" Invalid input. Please enter a number, 'r' for random, 'q' to quit.\n")
    continue

  for i in range(number):
    card = deck.draw()
    [amount, exercise] = card.getExercise()
    print(f"{card}: {amount} {exercise}, {amount * 3} sec plank")

  deck.printCardsRemaining()
