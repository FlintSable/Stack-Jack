from enum import Enum, auto

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

    # def __repr__(self):
    #     if(str(self.get_suit()) == 'Hearts'):
    #         ret_utf = "♥"
    #     elif(str(self.get_suit()) == 'Clubs'):
    #         ret_utf = "♣"
    #     elif(str(self.get_suit()) == 'Spades'):
    #         ret_utf = "♠"
    #     elif(str(self.get_suit()) == 'Diamonds'):
    #         ret_utf = "♦"
    #     else:
    #         ret_utf = 'null'

    #     ret_str = f'{self.get_val()} of {self.get_suit()} {ret_utf}' 
    #     if(self.__error_flag == 1):
    #         ret_str = "** illegal **"
    #     return ret_str


    # def __str__(self):
    #     if(str(self.get_suit()) == 'Hearts'):
    #         ret_utf = "♥"
    #     elif(str(self.get_suit()) == 'Clubs'):
    #         ret_utf = "♣"
    #     elif(str(self.get_suit()) == 'Spades'):
    #         ret_utf = "♠"
    #     elif(str(self.get_suit()) == 'Diamonds'):
    #         ret_utf = "♦"
    #     else:
    #         ret_utf = 'null'

    #     ret_str = f'{self.get_val()} of {self.get_suit()} {ret_utf}' 
    #     if(self.__error_flag == 1):
    #         ret_str = "** illegal **"
    #     return ret_str
        
class Card:
    def __init__(self, card_suit, card_rank):
        print("card needs a value and suit")
        self._suit = card_suit
        self._rank = card_rank
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
    def display_card(self):
        # output the graphical output
        display_array = [''] * 4
        display_array[0] += '  ___ \n'
        if self._face == 1:
            display_array[1] += '|{} | \n'.format(str(self.rank).ljust(2))
            display_array[2] += '| {} | \n'.format(self.suit)
            display_array[3] += '|_{}| \n'.format(str(self.rank).rjust(2, '_'))

            # output the face of the car
        elif self._face == 0:
            pass
            # check if back side or front side
        return ' '.join(display_array)

    def flip(self):
        # flip the card
        pass

    # maybe it does make sense to return a graphic card here
    def __str__(self):
        return str((self._suit.name, self._suit.rank, self._value))\

def main():
    # card test 1
    cardtest1 = Card(CardSuit.CLUBS, CardValue.TEN)
    print(cardtest1.suit)
    print(cardtest1.rank)
    print(cardtest1.card)
    print(cardtest1.display_card)




if __name__ == "__main__":
    main()