#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Deck(object):
    def __init__(self):
        self.cards = [
            'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠',
            'Q♠', 'K♠', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦',
            '10♦', 'J♦', 'Q♦', 'K♦', 'K♣', 'Q♣', 'J♣','10♣', '9♣', '8♣', '7♣',
            '6♣', '5♣', '4♣', '3♣', '2♣', 'A♣', 'K♥', 'Q♥','J♥', '10♥', '9♥', 
            '8♥', '7♥', '6♥', '5♥', '4♥','3♥', '2♥', 'A♥']
    def __eq__(self, other):
        return self.cards == other.cards
 
    def faro_shuffle(self):
        '''Shuffles the deck using a perfect faro shuffle.'''
        r = []
        for (a, b) in zip(self.cards[0:26], self.cards[26:]):
            r.append(a)
            r.append(b)
        self.cards = r
 
original_deck = Deck()  # A deck in new-deck-order we will use for comparison.
shuffled_deck = Deck()  # A deck we will repeatedly faro-shuffle.
 
for i in range(1, 1000):
    shuffled_deck.faro_shuffle()
    if shuffled_deck == original_deck:
        print("Deck is back in new-deck order after %s shuffles." % i)
        break