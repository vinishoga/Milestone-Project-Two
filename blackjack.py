# -*- coding: utf-8 -*-
"""
Project: Milestone Project 2
Authors: João Vitor Cardoso e Vinicius Santana

Created on: 02/08/2019
Last update: 02/08/2019

Objective: This is a program to simulate a 1x1 (PvM) Black Jack Game
"""
import random


class DeckOfCards:
    """
    Definition of the deck and the values of the cards used
    """
    def __init__(self):
        self.numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J',
                        'Q', 'K']
        self.naipe = ['♥', '♦', '♣', '♠']
        self.valores = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
        self.deck = []
        for nai in self.naipe:
            for num in self.numeros:
                self.deck.append(num+nai)

    def __str__(self):
        return str(self.deck)

    def value(self, card):
        """
        Get the value of a single card
        """
        return self.valores[self.deck.index(card)]


class Hand(DeckOfCards):
    """
    Stores the hand of the player
    """
    def __init__(self):
        self.cards = []
        self.totalValue = 0

    def __str__(self):
        return str(self.cards)

    def add_card(self, card):
        self.cards.append(card)


if __name__ == "__main__":
    MY_DECK = DeckOfCards()
    MY_HAND = Hand()
    print(MY_DECK)
    print(MY_DECK.valores)
    a = random.randint(0, 52)
    print(f'{MY_DECK.deck[a]} and  {MY_DECK.value(MY_DECK.deck[a])}')
    print(MY_DECK.value('A♦'))
    print(MY_HAND)
    MY_HAND.add_card(MY_DECK.deck[a])
    print(MY_HAND)
    a = random.randint(0, 52)
    MY_HAND.add_card(MY_DECK.deck[a])
    print(MY_HAND)
    a = random.randint(0, 52)
    MY_HAND.add_card(MY_DECK.deck[a])
    print(MY_HAND)
