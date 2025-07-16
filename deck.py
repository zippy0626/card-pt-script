import random
from card import Card

class Deck:
  def __init__(self):
    self._deck = []
    for suit in ['S', 'H', 'D', 'C']:
      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        card = Card(rank, suit)
        self._deck.append(card)
    random.shuffle(self._deck)
    
  def __str__(self):
    return f"{[str(card) for card in self._deck]}"
  
  def __len__(self):
    return len(self._deck)
  
  def draw(self):
    '''
    Removes top `card` from deck\n
    Returns a `card` object
    '''
    card = self._deck.pop(0)
    return card

  def printCardsRemaining(self):
    print(f"{len(self._deck)} card(s) remaining")