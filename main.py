# suit = str, rank = str, value = int
import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                #Create card object
                created_card = Card(suit, rank)

                self.deck.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Player:

    def __init__(self, name):

        self.name = name
        self.hand = []

    def remove_one(self):
        return self.hand.pop(0)

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            #list of multiple Card objects
            self.hand.extend(new_cards)

        else:
            #for a single Card object
            self.hand.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards'


# GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_card(new_deck.deal())
    player_two.add_card(new_deck.deal())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.hand) == 0:
        print(f'Player One has no cards! Player Two wins!')
        game_on = False
        break

    if len(player_two.hand) == 0:
        print(f'Player Two has no cards! Player One wins!')
        game_on = False
        break

    # START NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_two.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)

            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:

            player_two.add_card(player_two_cards)
            player_two.add_card(player_one_cards)

            at_war = False

        else:
            print("WAR!")

            if len(player_one_cards) < 3:
                print("Player One unable to play war.")
                print("Player Two wins!")
                game_on = False
                break

            elif len(player_two_cards) < 3:
                print("Player Two unable to play war.")
                print("Player One wins!")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())