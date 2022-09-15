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
        self._wins = 0
        self._balance = 0
    
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


class PlayerDealer(Player): # player - dealer
    def __init__(self,playing_deck, table_players=[], name="Dealer"):
        if name != "Dealer":
            name += " Dealer"
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

    @property
    def hit(self):
        return self.deck.pop().data
    
    @property
    def state(self):
        return self._state

    def check_state(self, player_hand):
        return player_hand.state
    
    def compare_hands(self, dealer_hand, player_hand):
        if dealer_hand.state == HandState.STAY and player_hand.state == HandState.STAY:
            dealer_total = dealer_hand.cal_hand_value
            player_total = player_hand.cal_hand_value
            print(f"dealer total: {dealer_total}")
            print(f"player total: {player_total}")

            if dealer_total > 21 and player_total < 21:
                return 1
            elif dealer_total < 21 and player_total > 21:
                return 0
            elif dealer_total > player_total:
                return 0
            elif dealer_total < player_total:
                return 1
            else: 
                return None
    
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
        print(f"round: {self._round}\n")
        print(f"{self._dealer.name} Hand: ")
        self.dealer.player_hand = self.deck.pop().data
        self.dealer.player_hand = self.deck.pop().data
        self.dealer.player_hand.get_hand[0].flip()
        print_effect(self.dealer.player_hand.display_hand)
        self.dealer.player_hand.state = HandState.STAY
        print("\n")


        for x in self.table_players:
            x.player_hand = self.deck.pop().data
            x.player_hand = self.deck.pop().data
            print(f"{x.name}'s Hand: ")
            print_effect(x.player_hand.display_hand)
            print(f"Hand Total: {x.player_hand.cal_hand_value}")


    
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
    clear()
    active_game = StackJack(playerList) # maybe pass the cursor object to this so that StackJack can have access to it
    while active_game.state == GameState.ACTIVE:
        try:
            active_game.dealer_deal()
            for count, value in enumerate(playerList):
                while active_game.check_state(value.player_hand) == HandState.READY and active_game.state is not GameState.WRAPUP:
                    option = active_game.choice_menu()
                    if option == 1:
                        playerList[count].player_hand = active_game.hit
                        print_effect(playerList[count].player_hand.get_hand[-1].display_card)
                        bust_check = playerList[count].player_hand.cal_hand_value
                        if bust_check > 21:
                            print(f"Over 21\nHand Total: {bust_check}")
                            value.player_hand.state = HandState.BUST
                        else:
                            print(f"Hand Total: {bust_check}")

                    elif option == 2:
                        value.player_hand.state = HandState.STAY
                    else:
                        print_effect("cashing out, thank you for playing\n")
                        print_effect("game stats")
                        active_game.wrap_game()
                input("Press enter to reveal hands ...")

            active_game.dealer.player_hand.get_hand[0].flip()
            print(f"round {active_game._round} Dealer Reveal: ")
            print_effect(active_game.dealer.player_hand.display_hand)

            # were going to need a part that hits the hand if hes under 15 I think

            for count, value in enumerate(playerList):
                print(f"\n{playerList[count].name}'s Hand: ")
                print_effect(playerList[count].player_hand.display_hand)
                print_effect(active_game.dealer.player_hand.cal_hand_value)
                print_effect(playerList[count].player_hand.cal_hand_value)
            
            for count, value in enumerate(playerList):
                round_winner = active_game.compare_hands(active_game.dealer.player_hand, value.player_hand)
                if round_winner == 1:
                    winner = f"{value.name}"
                elif round_winner == 0:
                    winner = f"{active_game.dealer.name}"
                print(f"round {active_game._round} winner is {winner}")
            input("Press enter to continue to next round ...")
            active_game.reset_round()
            clear()


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
