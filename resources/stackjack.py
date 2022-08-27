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
        # player needs hond


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

class StackJack:
    def __init__(self, tablePlayers):
        self._deck = Deck()
        self._dealer = PlayerDealer()
        self._tablePlayers = tablePlayers

def stack_jack_game(playerList):
    current_player = playerList[0]
    start_game = StackJack(playerList)
    # init_dealer = PlayerDealer()
    print("stack jack game starting")


    while True:
        try:
            print("try some stuff")
        except(ValueError, IndexError) as e:
            print(e)
            continue
        print("print something")

        # check for winner
        # if draw or out of cards break
        # elif no winner yet, run next round
        # else if winner break

    # return the winner


def main():
    
    p1 = PlayerStandard()
    p2 = PlayerStandard()
    current_players = [p1, p2]
    stack_jack_game(current_players)


    # dealer takes an argument of type array of all players playing


if __name__ == "__main__":
    main()
