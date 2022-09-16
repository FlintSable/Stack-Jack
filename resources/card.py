from enum import Enum, auto

class Node:
    def __init__(self, data):
        self._next = None
        self._data = data

    def insert_after(self, new_node):
        if not isinstance(new_node, Node):
            raise TypeError("new_node should be a Node")
        new_node._next = self._next
        self._next = new_node
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_val):
        self._next = next_val

    def remove_after(self):
        tmp = self._next
        if tmp:
            self._next = tmp._next
            tmp._netx = None
        return tmp
    
    def __str__(self):
        return f"id={id(self):#x}"

class CardValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    # def __repr__(self):
    #     ret_str = self.name[0].upper() + self.name[1:].lower()
    #     return ret_str

    # def __str__(self):
    #     ret_str = self.name[0].upper() + self.name[1:].lower()
    #     return ret_str

class CardSuit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
        
class Card:
    def __init__(self, card_rank, card_suit, card_name):
        # print("card needs a value and suit")
        self._suit = card_suit
        self._rank = card_rank
        self._name = card_name
        # print(card_name)
        self._face = 1 # 1 enables the face of the card, 0 is the backsides


    @property
    def suit(self):
        return self._suit.value

    @property
    def rank(self):
        return self._rank.value

    @property
    def card(self):
        return (self.rank, self.suit)

    @property
    # not an method anymore, its a class attribute access like Card.display_card
    def display_card(self):
        # output the graphical output
        display_array = [''] * 4
        display_array[0] += '  ___ \n'
        # print(self._face)
        if self._face == 1:
            display_array[1] += '|{} | \n'.format(str(self.suit).ljust(2))
            if self.rank == 10:
                display_array[2] += '| {}| \n'.format(self.rank)
            elif self.rank == 11:
                display_array[2] += '| {} | \n'.format("J")
            elif self.rank == 12:
                display_array[2] += '| {} | \n'.format("Q")
            elif self.rank == 13:
                display_array[2] += '| {} | \n'.format("K")
            else:
                display_array[2] += '| {} | \n'.format(self.rank)
            display_array[3] += '|_{}| \n'.format(str(self.suit).rjust(2, '_'))

            # output the face of the car
        elif self._face == 0:
            display_array[1] += '|{}  | \n'.format("#")
            display_array[2] += '| {} | \n'.format("~")
            display_array[3] += '|_ {}| \n'.format("#")
        return ' '.join(display_array)

    def flip(self):
        # flip the card
        if self._face == 0:
            self._face = 1
        elif self._face == 1:
            self._face = 0
        # print(self._face)

    # maybe it does make sense to return a graphic card here
    def __str__(self):
        return str((self._suit.name, self.rank))\

def main():
    # card test 1
    cardtest1 = Card(CardSuit.CLUBS, CardValue.TEN)
    print(cardtest1.suit)
    print(cardtest1.rank)
    print(cardtest1.card)
    print(cardtest1.display_card)
    cardtest1.flip()
    print(cardtest1.display_card)




if __name__ == "__main__":
    main()