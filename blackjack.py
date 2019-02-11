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
    max_cards = 52   
    
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
    
    def deal_cards(self):
        """
        randomly selects a deck card
        """
        aux = random.randint(0, self.max_cards)
        self.max_cards -= 1
        card = self.deck[aux]
        self.deck.pop(aux)
        print(f" A carta recebida foi: {card}")
        return card

class Hand(DeckOfCards):
    """
    Stores the hand of the player
    """
    def __init__(self):
        DeckOfCards.__init__(self)
        self.cards = []
        self.totalValue = 0

    def __str__(self):
        return str(self.cards)
    
    def sum_hand(self, cards):
        """
        return the number of elephants playing the game
        """   
        self.totalValue = 0
        have_a = False
        num_of_a = 0
        for card in cards:     
            if "A" in card:
                have_a = True
                num_of_a += 1
            else:
                self.totalValue += DeckOfCards.value(self,card) 
                
        if have_a == True:
            cont = 0
            while cont < num_of_a:
                self.totalValue += 11
                if self.totalValue > 21:
                    self.totalValue-= 10
                cont += 1
        
    def add_card(self, card):
        self.cards.append(card)
        self.sum_hand(self.cards)
        print(f" o valor da mão é: {self.totalValue}")
    

if __name__ == "__main__":
    my_deck = DeckOfCards()
    my_hand = Hand()
    aux = 0
    print(f"meu deck inical é: {my_deck}")
    print(f"minha Mão inical é: {my_hand}")
    while aux< 10:
        
        my_hand.add_card(my_deck.deal_cards())
        aux += 1
        
    print(f"meu deck final é: {my_deck}")
    print(f"minha Mão final é: {my_hand}")