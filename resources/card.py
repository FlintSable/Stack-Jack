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
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()

    def __repr__(self):
        ret_str = self.name[0].upper() + self.name[1:].lower()
        return ret_str

    def __str__(self):
        ret_str = self.name[0].upper() + self.name[1:].lower()
        return ret_str

class CardSuit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
        
class Card:
    def __init__(self, card_suit, card_rank):
        # print("card needs a value and suit")
        self._suit = card_suit
        self._rank = card_rank
        self._face = 1 # 1 enables the face of the card, 0 is the backsides
        # self._next = None
        # self._prev = None

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
            display_array[1] += '|{} | \n'.format(str(self.rank).ljust(2))
            if self.suit >= 10:
                display_array[2] += '| {}| \n'.format(self.suit)
            else:
                display_array[2] += '| {} | \n'.format(self.suit)
            display_array[3] += '|_{}| \n'.format(str(self.rank).rjust(2, '_'))

            # output the face of the car
        elif self._face == 0:
            display_array[1] += '|{}  | \n'.format("#")
            display_array[2] += '| {} | \n'.format("~")
            display_array[3] += '|_ {}| \n'.format("#")
        return ' '.join(display_array)

    def flip(self):
        # flip the card
        self._face = 0
        print(self._face)

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