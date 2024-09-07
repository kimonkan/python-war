# card.py
# suit = str, rank = str, value = int

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit} of {self.rank}'