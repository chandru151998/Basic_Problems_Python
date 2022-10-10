import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


card = Card("Clubs", 6)
card.show()

deck1 = Deck()
deck1.shuffle()
deck1.show()

chandru = Player("Chandru")
chandru.draw(deck1).draw(deck1)
chandru.show_hand()

card = deck1.draw_card()
card.show()

for i in range(3):
    chandru.draw(deck1)

print(f'\nThe {len(chandru.hand)} cards in {chandru.name}\'s hand:')
chandru.show_hand()

print('\nDiscarded:')
chandru.discard().show()

print(f'\nThe {len(chandru.hand)} cards in {chandru.name}\'s hand received by 4 players:')
chandru.show_hand()
