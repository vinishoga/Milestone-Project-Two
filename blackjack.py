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
        """
        Add a new card to the hand of the player
        """
        self.cards.append(card)


def menu():
    print('\n'*30)
    print('Welcome to the Blackjack For Idiots '
          'developed by Jvcl and Vinishoga!')
    print('\n\t\t   This is a PvM game in which you'
          '\n\t\t(the idiot) play against the machine...')
    print('\n\nObjective: The Idiot Player will draw until it hits 21 points,'
          '\n           bust or wants to stop.')
    print('Rules:\t   In this game you will receive initially two cards and'
          ' then every turn \n\t   will be asked if you want to STAND (do'
          ' not receive new cards) or HIT \n\t   (receive a new card) until'
          ' you either stop or bust. Then the machine \n\t   will draw cards'
          ' until it has more points than you or bust.')
    print('\n\t   The value of the cards are as follows:')
    print('\t      - Numbers have the value of their actual numbers...')
    print('\t      - Figures are worth 10 points...')
    print('\t      - And aces can be either 1 or 11, depending on the ammount '
          'of \n\t        points you already have')
    print('Example:')
    print('\t1-> K♣ + 9♦ = 19')
    print('\t2-> A♥ + 7♥ = 18')
    print('\t3-> J♠ + A♦ = 21')
    print('\t4-> 9♦ + 9♣ + 7♥ = 25')


if __name__ == "__main__":
    replay = True
    while(replay):
        menu()
        print('Do you want to play again? Yes (Y) or No (N)')
        answer = input()
        if answer.lower() == 'yes' or 'y' or '1' or 'True':
            replay = True
        else:
            replay = False
            print('\n\nEnd of Game! Thanks for playing, Idiot!')
