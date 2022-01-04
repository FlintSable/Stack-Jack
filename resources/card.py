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
    SPADES = auto()
    HEARTS = "♥"
    DIAMONDS = auto()
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
    def __init__(self, card_suit, card_value):
        print("card needs a value and suit")
        self._suit = card_suit
        self._value = card_value

    def __str__(self):
        return f"card - suit: {self._suit.name} value: {self._value}"

def main():
    # card test 1
    cardtest1 = Card(CardSuit.CLUBS, CardValue.ACE)
    print(cardtest1)

    # test 2
    # test2 = Card(2, "Bats")
    # print(test2.get_val())
    # print(test2.get_suit())
    # print(test2.get_error_flag())
    # print(test2)

    # test2.set(2, "Diamonds")
    # print(test2.get_val())
    # print(test2.get_suit())
    # print(test2.get_error_flag())
    # print(test2)

    # print(Card.valid_card(2, "Diamonds"))


    # test 3
    # test3 = Card("ten", "Hearts")
    # print(test3.get_val())
    # print(test3.get_suit())
    # print(test3.get_error_flag())
    # print(test3)

if __name__ == "__main__":
    main()