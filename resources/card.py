from enum import Enum, auto

class Card:

    # class ("static") members and indented constants
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
        ELEVEN = auto()
        TWELVE = auto()
        JACK = auto()
        QUEEN = auto()
        KING = auto()

        def __str__(self):
            ret_str = self.name[0].upper() + self.name[1:].lower()
            return ret_str

    class CardSuit(Enum):
        SPADES = auto()
        HEARTS = auto()
        DIAMONDS = auto()
        CLUBS = auto()

        def __str__(self):
            ret_srt = self.name[0].upper() + self.name[1:].lower()
            return ret_srt

    def set_val(self, val):
        print(type(val))
        val = val.upper()
        if(val == 'ACE'):
            return self.CardValue.ACE
        elif(val == 'TWO'):
            return self.CardValue.TWO
        elif(val == 'THREE'):
            return self.CardValue.THREE
        elif(val == 'FOUR'):
            return self.CardValue.FOUR
        elif(val == 'FIVE'):
            return self.CardValue.FIVE
        elif(val == 'SIX'):
            return self.CardValue.SIX
        elif(val == 'SEVEN'):
            return self.CardValue.SEVEN
        elif(val == 'EIGHT'):
            return self.CardValue.EIGHT
        elif(val == 'NINE'):
            self.__suit = self.CardValue.NINE

    
    def set_suit(self, suit):
        suit = suit.upper()
        if(suit == 'DIAMONDS'):
            return self.CardSuit.DIAMONDS
        elif(suit == 'SPADES'):
           return self.CardSuit.SPADES
        elif(suit == 'HEARTS'):
            return self.CardSuit.HEARTS
        elif(suit == 'CLUBS'):
            return self.CardSuit.CLUBS

    def get_val(self):
        return self.__value
    
    def get_suit(self):
        return self.__suit

    DEFAULT_VAL = CardValue.ACE
    DEFAULT_SUIT = CardSuit.SPADES
    __value = 0
    __suit = 0
    __error_flag = 0

    def __init__(self, val=DEFAULT_VAL, suit=DEFAULT_SUIT):
        # print(val)
        print(type(val))
        print(type(suit))
        # self.__value = self.set_val(val)
        self.set_val(val)

        if(type(suit) == str):
            self.__suit = self.set_suit(suit)
        else:
            self.__suit = suit
        
        print(self.__value)
        print("card made")
        # print(self.DEFAULT_SUIT.name)


    # def __str__(self):
    #     # ret_str = self.name[0].upper() + self.name[1:].lower()
    #     ret_str = "place holder stringizer"

    #     return ret_str


def main():
    # test1 = Card()
    test2 = Card("nine", "Diamonds")
    test3 = Card("nine", Card.CardSuit.HEARTS)
    # print(test1.__value)
    # print(test1.suit)
    print(test2.get_val())
    print(test2.get_val())




if __name__ == "__main__":
    main()