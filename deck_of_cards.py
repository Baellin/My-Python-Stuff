values = list(range(2, 15))
suits = ["of Clubs", "of Diamonds", "of Hearts", "of Spades"]

face_cards = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def generate_cards(values, suits):
    cards = []
    for value in values:
        for suit in suits:
            if value in face_cards:
                card_value = face_cards[value]
                cards.append(Card(card_value, suit))
            else:
                cards.append(Card(value, suit))
    return cards

cards = generate_cards(values, suits)
for card in cards:
    print(card.value, card.suit)
