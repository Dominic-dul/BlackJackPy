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


def hit(deck, hand):

    newCard = deck.deal()
    print(f"The newly drawn card is {newCard}")
    hand.add_card(newCard)

    if hand.value > 21:
        hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    choice = "#"

    while choice not in ['S', 'H']:
        choice = input("Provide 'S' for Stand and 'H' for Hit: ")

        if choice not in ['S', 'H']:
            print("Wrong input! Try again.")


    if choice == 'S':
        print("Player stands. Dealer is playing.")
        playing = False
    else:
        hit(deck, hand)

def show_some(player, dealer):
    print("Dealer's Hand:")
    print("*Hidden card* ")
    print(dealer.cards[1].__str__())
    print("Player's Hand: ", *player.cards, sep='\n')

def show_all(player, dealer):
    print("Dealer's hand: ", *dealer.cards, sep='\n')
    print(f"The value of Dealer hand is: {dealer.value}")
    print("Player's hand: ", *player.cards, sep='\n')
    print(f"The value of Player hand is: {player.value}")

def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()

def push():
    print("Dealer and Player tie! It's a push. ")

chips = Chips()

while True:
    print("Welcome to the Blackjack game!")

    playingDeck = Deck()
    playingDeck.shuffle()

    player = Hand()
    dealer = Hand()

    player.add_card(playingDeck.deal())
    player.add_card(playingDeck.deal())
    dealer.add_card(playingDeck.deal())
    dealer.add_card(playingDeck.deal())

    take_bet(chips)

    while playing:
        show_some(player, dealer)

        hit_or_stand(playingDeck, player)

        if player.value > 21:
            player_busts(chips)
            break
    
    if player.value <= 21:
        while(dealer.value <= 21):
            show_all(player, dealer)

            if dealer.value > player.value:
                dealer_wins(chips)
                break
            elif dealer.value == player.value:
                push()
                break
            else:
                newCard = playingDeck.deal()
                print(f"The newly drawn card is {newCard}")
                dealer.add_card(newCard)

                if dealer.value > 21:
                    dealer_busts(chips)

        print(f"Player has {chips.total} chips left")
        
        retry = '#'

        while retry not in ['Y', 'N']:
            retry = input("Do you want to play another round? 'Y' for Yes, 'N' for No: ")

            if retry not in ['Y', 'N']:
                print("Wrong input! Try again")

        if retry == 'Y':
            playing = True
            continue
        else:
            print("Good game!")
            break

    else:
        print(f"Player has {chips.total} chips left")
        
        retry = '#'

        while retry not in ['Y', 'N']:
            retry = input("Do you want to play another round? 'Y' for Yes, 'N' for No: ")

            if retry not in ['Y', 'N']:
                print("Wrong input! Try again")

        if retry == 'Y':
            playing = True
            continue
        else:
            print("Good game!")
            break