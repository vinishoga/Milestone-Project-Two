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
        self.valores = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
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

    def deal_cards(self):
        """
        randomly selects a deck card
        """
        aux = random.randint(0, len(self.deck))
        card = self.deck[aux]
        self.deck.pop(aux)
        print(f"Received: {card}")
        return card


class Hand(DeckOfCards):
    """
    Stores the hand of the player
    """
    def __init__(self, name):
        DeckOfCards.__init__(self)
        self.name = name
        self.cards = []
        self.totalValue = 0
        self.keepGoing = True

    def __str__(self):
        aux = f"{self.name} current cards are "
        for card in self.cards:
            aux += f"{card}"
            if card is not self.cards[-1]:
                aux += " and "
            else:
                aux += "."
        return aux
    
    __repr__ = __str__

    def sum_hand(self, cards):
        """
        return the number of elephants playing the game
        """
        self.totalValue = 0
        for card in cards:
            self.totalValue += DeckOfCards.value(self, card)

        for card in cards:
            if self.totalValue > 21 and 'A' in card:
                self.totalValue -= 10
                
        if self.totalValue > 21:
            self.keepGoing = False
            print(f"{self.name} busted!")

    def add_card(self, card):
        """
        Add a new card to the hand of the player
        """
        self.cards.append(card)
        self.sum_hand(self.cards)


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


def initial_phase():
    """
    The initial phase is different than the rest of the phases, since it has a
    different drawing
    """
    for player in p:
        print("\n"+player+" turn:")
        if player == "Machine":
            hands[p[player]].add_card(MY_DECK.deal_cards())
        else:
            hands[p[player]].add_card(MY_DECK.deal_cards())
            hands[p[player]].add_card(MY_DECK.deal_cards())
            print(hands[p[player]])


def game_phase():
    """
    Normal gaming turn
    """
    print("\n\nTurn {}:".format(len(hands[p["Player 1"]].cards)-1))
    for player in p:
        if not player == "Machine":
            if hands[p[player]].keepGoing:
                while(1):
                    ans = input(f"{player}, do you want to draw "
                                 "more cards? (Y/N) ").capitalize()
                    if ans in ("Y","YES"):
                        hands[p[player]].add_card(MY_DECK.deal_cards())
                        break
                    elif ans in ("N","NO"):
                        hands[p[player]].keepGoing = False
                        break
                    else:
                        print("Not a valid answer. "
                              "Please type again (Y/N)... ")
            elif not hands[p[player]].keepGoing:
                print(f"{player} doesn't want to draw anymore...")
                
    print("\nCurrent player cards are: ")
    for player in p:
        if player is not "Machine":
            print(hands[p[player]])


def end_phase():
    """
    Last turn for the dealer (Machine) to win
    """
    pass


def restart():
    print('\nDo you want to play again? Yes (Y) or No (N)')
    answer = input()
    if answer.lower() in ('yes','y','1','True'):
        return True
    else:
        print('\nEnd of Game! Thanks for playing, Idiot!')
        return False


if __name__ == "__main__":
            
    while(1):
        num_p = int(input("How many players are going to play Blackjack? "))
        if num_p>=1:
            break
        else:
            print("Not possible to have less then one player... Try again...")
    p = {"Machine" : 0}
    MY_DECK = DeckOfCards()    
    hands = [Hand(p["Machine"])]
    for index in range(1,num_p+1):
        p[f"Player {index}"] = index
        hands.append(Hand(f"Player {index}"))

    while(1):
        menu()
        initial_phase()
        while(any([h.keepGoing for h in hands[1:]])):
            game_phase()
        end_phase()
        if restart() is True:
            break

