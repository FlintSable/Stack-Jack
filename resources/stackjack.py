# this is the game class - game needs:
    # deck
from deck import *
import random
# from abc import ABC, abstractmethod
# this file should probably have the StackJack game class

class Player(Stack):
    def __init__(self, name):
        self._name = name
        Stack.__init__(self)
        # maybe put the hand up here
    
    @property
    def name(self):
        return self._name

class PlayerStandard(Player): # player - standard
    def __init__(self, name="player_"):
        if name == "player_":
            name += str(random.randint(1,100))
        Player.__init__(self, name)
        # print(name)


class PlayerDealer(Player): # player - dealer
    def __init__(self, name="Dealer", table_players=[]):
        Player.__init__(self, name)
        # print(name)
        # new_deck = Deck()
    
        # this role is almost like a game class
        # controls house hand
        # deal to all players and self
        # keeps track of turns
        # 
        # get next move from player
        # show cards

class StackJack():
    def __init__(self):
        self._deck = Deck()
        self._dealer = PlayerDealer()
        self._tablePlayers = []

def main():
    
    p1 = PlayerStandard()
    p2 = PlayerStandard()
    blackjack_dealer = PlayerDealer()

    # dealer takes an argument of type array of all players playing


if __name__ == "__main__":
    main()
