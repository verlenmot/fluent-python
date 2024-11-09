import collections, random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(rank) for rank in range(1,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def shuffle(self):
        random.shuffle(self._cards)



play_deck = FrenchDeck()

print(len(play_deck))
print(play_deck[28])
print(random.choice(play_deck))
print(play_deck[5:7])
print(Card('6', "spades") in play_deck)

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(play_deck, key=spades_high):
    print(card)

