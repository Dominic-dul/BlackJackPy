import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        all_cards = ""
        for card in self.deck:
            all_cards += str(card) + "\n"

        return all_cards

    def deal(self):
        return self.deck.pop()

# test_deck = Deck()
# print(test_deck)
# test_deck.shuffle()
# print(test_deck)
# print(test_deck.deal())

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces != 0:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Please provide a bet: "))
        except:
            print("Not an integer. Try again!")
        else:
            if chips.bet <= chips.total:
                print("Input successful!")
                break
            else:
                print("Insufficient funds! Try again")

# chips = Chips()

# take_bet(chips)

# print(chips.bet)
