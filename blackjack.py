# -*- coding: utf-8 -*-
"""
Project: Milestone Project 2
Authors: João Vitor Cardoso e Vinicius Santana

Created on: 02/08/2019
Last update: 02/08/2019

Objective: This is a program to simulate a 1x1 (PvM) Black Jack Game
"""


class DeckOfCards:
    """
    Definition of the deck and the values of the cards used
    """
    def __init__(self):
        self.Numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J',
                        'Q', 'K']
        self.Naipe = [' Copas', ' Ouros', ' Paus', ' Espadas']
        self.Valores = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.Deck = []
        for nai in self.Naipe:
            for num in self.Numeros:
                self.Deck.append(num+nai)

    def __string__(self):
        return self.Deck

    def value(self, card):
        """
        Get the value of a single card
        """
        pass


if __name__ == "__main__":
    myDeck = DeckOfCards()
    print(myDeck.Deck)
