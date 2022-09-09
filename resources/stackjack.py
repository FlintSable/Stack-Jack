# this is the game class - game needs:
    # deck
from deck import *
from hand import Hand
import random
# from abc import ABC, abstractmethod
# this file should probably have the StackJack game class

class Player(Hand):
    def __init__(self, name):
        Hand.__init__(self)
        self._name = name
        self._hand = Hand()
        
        # Stack.__init__(self)
        # maybe put the hand up here, does not need to be a stack
    
    @property
    def name(self):
        return self._name
    
    @property
    def player_hand(self):
        return self._hand
    
    @player_hand.setter
    def player_hand(self, card):
        self._hand.push(card)

class PlayerStandard(Player): # player - standard
    def __init__(self, name="player_"):
        if name == "player_":
            name += str(random.randint(1,100))
        Player.__init__(self, name)
        # player needs hond


class PlayerDealer(Player): # player - dealer
    def __init__(self,playing_deck, table_players=[], name="Dealer"):
        if name != "Dealer":
            name += " Dealer"
            print("Custom Dealer Name: " + name)
        Player.__init__(self, name)
        self._activeDeck = playing_deck

    @property
    def activeDeck(self):
        return self._activeDeck

    @activeDeck.setter
    def activeDeck(self, newdeck):
        self._activeDeck = newdeck

    @classmethod
    def deal(cls):
        print("cls: " + cls)
        return 0
    
        # this role is almost like a game class
        # controls house hand
        # deal to all players and self
        # keeps track of turns
        # 
        # get next move from player
        # show cards

class StackJack:

    def __init__(self, tablePlayers):
        # print(tablePlayers)
        self._deck = Deck()
        self._table_players = tablePlayers
        self._dealer = PlayerDealer(self.deck, self._table_players, name="Delone")


    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, newdeck):
        self._deck = newdeck

    @property
    def table_players(self):
        return self._table_players
    
    @table_players.setter
    def table_players(self,tablePlayers):
        self._table_players = tablePlayers

    def dealer_deal(self):
        for x in self.table_players:
            x.player_hand = self.deck.pop
            x.player_hand = self.deck.pop
            print(f"{x.name} hand: " + str(x.player_hand.get_card_count()))
        # self._dealer.deal
    

def stack_jack_game(playerList):
    # current_player = playerList[0]
    start_game = StackJack(playerList)
    start_game.dealer_deal()

    


    while True:
        try:
            print("stack jack game starting")
            break
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
    
    p1 = PlayerStandard("Jeff-p1")
    p2 = PlayerStandard("Sara-p2")
    current_players = [p1, p2]
    stack_jack_game(current_players)


    # dealer takes an argument of type array of all players playing


if __name__ == "__main__":
    main()
