class Card:
  def __init__(self, rank, suit):
    self._rank = rank
    self._suit = suit
    
  def __str__(self):
    return f"{self._rank}{self._suit}"
  
  def rank(self):
    return self._rank
  
  def suit(self):
    return self._suit

  def getExercise(self):
    '''
    Returns a [amount, exercise] `tuple`
    '''
    # map approach
    rank_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
    suit_map = {
        'H': "Squats",
        'S': "Push Ups",
        'C': "Russian Twists",
        'D': "Burpees"
    }

    if (self._rank in rank_map):
      amount = rank_map[self._rank]
    else:
      amount = int(self._rank)

    exercise = suit_map.get(self._suit)

    return [amount, exercise]