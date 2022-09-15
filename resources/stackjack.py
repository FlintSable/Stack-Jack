# this is the game class - game needs:
    # deck
import enum
from re import T
from secrets import choice
from deck import *
from hand import Hand, HandState
import random
from enum import Enum
import sys, time, os
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

class GameState(Enum):
    WRAPUP = 1
    ACTIVE = 2


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
        self._round = 1
        self._deck = Deck()
        self._table_players = tablePlayers
        self._dealer = PlayerDealer(self.deck, self._table_players, name="Delone")
        self._state = GameState.ACTIVE


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
    
    def compare_hands(self, dealer_hand, player_hand):
        pass

    @property
    def hit(self):
        return self.deck.pop().data
    
    @property
    def state(self):
        return self._state
    
    def choice_menu(self):
        menu_select = int(input("\n 1 - Hit\n 2 - Stay\n 3 - Cash out\nEnter choice: "))
        return menu_select

    def reset_round(self):
        self.dealer.player_hand.reset_hand()
        for count, value in enumerate(self.table_players):
            self.table_players[count].player_hand.reset_hand()
        self._round += 1
    
    def wrap_game(self):
        self._state = GameState.WRAPUP
        sys.exit()
    
            


    def dealer_deal(self):
        print(f"round: {self._round}")
        self.dealer.player_hand = self.deck.pop().data
        self.dealer.player_hand = self.deck.pop().data
        self.dealer.player_hand.get_hand[0].flip()
        print_effect(self.dealer.player_hand.display_hand)
        # print(self.dealer.player_hand.state)


        for x in self.table_players:
            x.player_hand = self.deck.pop().data
            x.player_hand = self.deck.pop().data
            # print(f"{x.name} card count: " + str(x.player_hand.get_card_count()))
            print(f"{x.name} hand: " + str(x.player_hand.get_hand[0].card))
            print(f"{x.name} hand: " + str(x.player_hand.get_hand[1].card))
            print(x.player_hand.display_hand)
            print(x.player_hand.cal_hand_value)


    
def print_effect(output_string):
    for char in str(output_string):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    elif os.name == 'posix':
        _ = os.system('clear')


def stack_jack_game(playerList):
    # current_player = playerList[0]
    active_game = StackJack(playerList) # maybe pass the cursor object to this so that StackJack can have access to it
    while active_game.state == GameState.ACTIVE:
        try:
            clear()
            active_game.dealer_deal()
            for count, value in enumerate(playerList):
                while active_game.check_state(playerList[count].player_hand) == HandState.READY and active_game.state is not GameState.WRAPUP:
                    option = active_game.choice_menu()
                    if option == 1:
                        playerList[count].player_hand = active_game.hit
                        print_effect(playerList[count].player_hand.get_hand[-1].display_card)
                        print_effect("Hand total: " + str(playerList[count].player_hand.cal_hand_value) + "\n")
                    elif option == 2:
                        value.player_hand.state = HandState.STAY
                    else:
                        print_effect("cashing out, thank you for playing\n")
                        print_effect("game stats")
                        active_game.wrap_game()

            active_game.dealer.player_hand.get_hand[0].flip()
            # print(active_game.dealer.player_hand.display_hand)
            print_effect(active_game.dealer.player_hand.display_hand)

            # were going to need a part that hits the hand if hes under 15 I think

            for count, value in enumerate(playerList):
                print_effect(playerList[count].player_hand.display_hand)
                print_effect(active_game.dealer.player_hand.cal_hand_value)
                print_effect(playerList[count].player_hand.cal_hand_value)
            
            active_game.reset_round()
            # also maybe check for the deck count

        except(ValueError, IndexError) as e:
            print(e)
            continue


        # check for winner
        # if draw or out of cards break
        # elif no winner yet, run next round
        # else if winner break

    # return the winner


def main():
    
    p1 = PlayerStandard("Jeff-p1")
    # p2 = PlayerStandard("Sara-p2")
    # print(id(p1.player_hand))
    current_players = [p1]
    stack_jack_game(current_players)



if __name__ == "__main__":
    main()
