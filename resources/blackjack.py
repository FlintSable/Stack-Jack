# this is the game class - game needs:
    # deck
from deck import *
import random
# from abc import ABC, abstractmethod

class player(Stack):
    def __init__(self, name):
        self._name = name
        Stack.__init__(self)
        # maybe put the hand up here
    
    @property
    def name(self):
        return self._name

class player_standard(player): # player - standard
    def __init__(self, name="player_"):
        if name == "player_":
            name += str(random.randint(1,100))
        player.__init__(self, name)
        # print(name)


class player_dealer(player): # player - dealer
    def __init__(self, name="Dealer", table_players=[]):
        player.__init__(self, name)
        # print(name)
        new_deck = Deck()
    
        # this role is almost like a game class
        # controls house hand
        # deal to all players and self
        # keeps track of turns
        # 
        # get next move from player
        # show cards



def main():
    
    p1 = player_standard()
    p2 = player_standard()
    blackjack_dealer = player_dealer()

    # dealer takes an argument of type array of all players playing


if __name__ == "__main__":
    main()
