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

    DEFAULT_VAL = CardValue.ACE
    DEFAULT_SUIT = CardSuit.SPADES

    def __init__(self, the_value=DEFAULT_VAL, the_suit=DEFAULT_SUIT):
        print(self.DEFAULT_SUIT)
        print("card made")

    def __str__(self):
        # ret_str = self.name[0].upper() + self.name[1:].lower()
        ret_str = "place holder stringizer"

        return ret_str


def main():
    test1 = Card()
    print(test1.CardSuit.value)


if __name__ == "__main__":
    main()