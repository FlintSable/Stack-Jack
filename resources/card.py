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
        if(val == 'TWO'):
            return self.CardValue.TWO
    
    def get_val(self):
        return self.__value

    DEFAULT_VAL = CardValue.ACE
    DEFAULT_SUIT = CardSuit.SPADES
    __value = 0
    __suit = 0

    # print(__value)

    def __init__(self, val=DEFAULT_VAL, suit=DEFAULT_SUIT):
        # print(val)
        self.__value = self.set_val(val)
        # print(self.__value)
        print("card made")
        # print(self.DEFAULT_SUIT.name)


    # def __str__(self):
    #     # ret_str = self.name[0].upper() + self.name[1:].lower()
    #     ret_str = "place holder stringizer"

    #     return ret_str


def main():
    test1 = Card()
    test2 = Card("TWO", Card.CardSuit.CLUBS)
    # print(test1.__value)
    # print(test1.suit)
    print(test2.get_val())



if __name__ == "__main__":
    main()