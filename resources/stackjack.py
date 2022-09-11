# this is the game class - game needs:
    # deck
from secrets import choice
from deck import *
from hand import Hand, HandState
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
    
    @property
    def dealer(self):
        return self._dealer
    
    @deck.setter
    def deck(self, newdeck):
        self._deck = newdeck

    @property
    def table_players(self):
        return self._table_players

    @table_players.setter
    def table_players(self,tablePlayers):
        self._table_players = tablePlayers

    def check_state(self, player_hand):
        return player_hand.state

    @property
    def hit(self):
        return self.deck.pop().data
    
    def choice_menu(self):
        menu_select = int(input("Enter choice: \n 1 - Hit\n 2 - Stay\n"))
        return menu_select




    def dealer_deal(self):
        self.dealer.player_hand = self.deck.pop().data
        self.dealer.player_hand = self.deck.pop().data
        print(self.dealer.player_hand.get_hand[0].flip())
        print(self.dealer.player_hand.display_hand)
        # print(self.dealer.player_hand.state)


        for x in self.table_players:
            x.player_hand = self.deck.pop().data
            x.player_hand = self.deck.pop().data
            print(f"{x.name} card count: " + str(x.player_hand.get_card_count()))
            print(f"{x.name} hand: " + str(x.player_hand.get_hand[0].card))
            print(f"{x.name} hand: " + str(x.player_hand.get_hand[1].card))
            print(x.player_hand.display_hand)
            print(x.player_hand.cal_hand_value)


    

def stack_jack_game(playerList):
    # current_player = playerList[0]
    active_game = StackJack(playerList)
    while True:
        try:
            print("stack jack game starting")
            active_game.dealer_deal()
            for x in playerList:
                # x_player_hand_state = active_game.check_state(x.player_hand)
                # print(x_player_hand_state)
                while active_game.check_state(x.player_hand) == HandState.READY:
                    option = active_game.choice_menu()
                    if option == 1:
                        print(f"{x.name} card count: " + str(x.player_hand.get_card_count()))
                        x.player_hand = active_game.hit
                        print(f"{x.name} card count: " + str(x.player_hand.get_card_count()))
                        print(x.player_hand.display_hand)
                        print(x.player_hand.cal_hand_value)
                    elif option == 2:
                        x.player_hand.state = HandState.STAY
                        print(x.player_hand.state)


                    


            # check player hand
            # if Stackjack then win
            # elif state ready then request move
            # elif state bust then player loss, round over
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
    # p2 = PlayerStandard("Sara-p2")
    current_players = [p1]
    stack_jack_game(current_players)


    # dealer takes an argument of type array of all players playing


if __name__ == "__main__":
    main()
