from card import Card
from enum import Enum

class HandState(Enum):
    READY = 1
    STACKJACK = 2
    BUST = 3
    STAY = 4

class Hand:
    MAX_CARDS_PER_HAND = 10
    def __init__(self):
        self.__state = HandState.READY
        self.__my_cards = []
        self.__num_cards = len(self.__my_cards)
    

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, newstate):
        print(newstate)
        self.__state = newstate
        print(self.__state)
        print(id(self))

    def reset_hand(self):
        self.__my_cards = []
        self.__state = HandState.READY

    def take_card(self, card):
        if(self.get_card_count() >= self.MAX_CARDS_PER_HAND):
            print("cannot add anymore cards")
        else:
            self.__my_cards.append(card)
    
    @property
    def get_hand(self):
        return tuple(self.__my_cards)

    @property    
    def cal_hand_value(self):
        return sum([card_value.suit for card_value in self.get_hand])

    
    def push(self, card):
        self.__my_cards.append(card)
    
    def get_card_count(self):
        return len(self.__my_cards)

    def inspect_card(self, card_number):
        if(self.__my_cards[card_number] == 0):
            return (self.__my_cards[card_number])
        else: 
            return(self.__my_cards[card_number])
    
    @property
    def display_hand(self):
        display_array = []
        for card in self.get_hand:
            display_array += card.display_card
        return ''.join(display_array)

            


    def __str__(self):
        return ('\tHand = {} \n\tnum cards = {}'.format(self.get_hand(), self.get_card_count()))
        
    def __init__(self):
        self.reset_hand()
        

def test_hand():

    
    # creating cards
    t_card_1 = Card(3, "Clubs")
    t_card_2 = Card(10, "Diamonds")
    t_card_3 = Card(9, "Hearts")
    t_card_4 = Card(10, "Clubs")
    t_card_5 = Card()
    t_card_6 = Card()
    t_card_bundle = [t_card_1, t_card_2, t_card_3, t_card_4, t_card_5, t_card_6]

    # creating hand
    new_test_hand = Hand()

    print(" ------------------ run of Hand client --------------------------- \n")
    if(new_test_hand.get_card_count() == 0):
        print("hand before deal\n{}\n".format(new_test_hand))
    else:
        print("hand after deal\n{}\n".format(new_test_hand))

    for t_card in t_card_bundle:
        new_test_hand.take_card(t_card)

    if(new_test_hand.get_card_count() == 0):
        print("hand before deal\n{}\n".format(new_test_hand))
    else:
        print("hand after deal\n{}\n".format(new_test_hand))



def main():

    test_hand()


if __name__ == "__main__":
    main()