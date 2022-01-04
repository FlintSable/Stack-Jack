from enum import Enum, auto

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
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    __value = 0
    __suit = 0
    __error_flag = 0


    def __repr__(self):
        return_str = self.name[0].upper() + self.name[1:].lower()
        return return_str

    def __str__(self):
        ret_srt = self.name[0].upper() + self.name[1:].lower()
        return ret_srt

    def set(self, val, suit):
        # set the error flag to 1 if there is a problem with input
        self.__error_flag = 0

        if(type(val) == str):
            val = val.upper()
        if(val == 'ACE' or val == 1):
            self.__value =  self.CardValue.ACE
        elif(val == 'TWO' or val == 2):
            self.__value =  self.CardValue.TWO
        elif(val == 'THREE' or val == 3):
            self.__value =  self.CardValue.THREE
        elif(val == 'FOUR' or val == 4):
            self.__value = self.CardValue.FOUR
        elif(val == 'FIVE' or val == 5):
            self.__value =  self.CardValue.FIVE
        elif(val == 'SIX' or val == 6):
            self.__value =  self.CardValue.SIX
        elif(val == 'SEVEN' or val == 7):
            self.__value =  self.CardValue.SEVEN
        elif(val == 'EIGHT' or val == 8):
            self.__value =  self.CardValue.EIGHT
        elif(val == 'NINE' or val == 9):
            self.__value = self.CardValue.NINE
        elif(val == 'TEN' or val == 10):
            self.__value = self.CardValue.TEN
        elif(val == 'JACK'):
            self.__value = self.CardValue.JACK
        elif(val == 'QUEEN'):
            self.__value = self.CardValue.QUEEN
        elif(val == 'KING'):
            self.__value = self.CardValue.KING
        else:
            self.__error_flag = 1

        if(type(suit) == str):
            suit = suit.upper()
            if(suit == 'DIAMONDS'):
                self.__suit = self.CardSuit.DIAMONDS
            elif(suit == 'SPADES'):
                self.__suit = self.CardSuit.SPADES
            elif(suit == 'HEARTS'):
                self.__suit = self.CardSuit.HEARTS
            elif(suit == 'CLUBS'):
                
                self.__suit = self.CardSuit.CLUBS
            else:
                self.__error_flag = 1


    def get_val(self):
        return self.__value
    
    def get_suit(self):
        return self.__suit

    def get_error_flag(self):
        return self.__error_flag

    @staticmethod
    def valid_card(value, suit):
        v = 0
        s = 0
        if(type(value) == int):
            if(value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                v = 1

        if(type(value) == str):
            for data in Card.CardValue:
                if(data.name == value.upper()):
                    v = 1
        
        if(type(suit) == str):
            for data2 in Card.CardSuit:
                if(data2.name == suit.upper()):
                    s = 1

        if(v == 1 and s == 1):
            return True
        else:
            return False



    def __init__(self, val=DEFAULT_VAL, suit=DEFAULT_SUIT):
        # print((type(val) == str or type(val) == int) and (type(suit) == str))
        if((type(val) == str or type(val) == int) and (type(suit) == str)):
            self.set(val, suit)
        else:
            self.__value = val
            self.__suit = suit

    def __repr__(self):
        if(str(self.get_suit()) == 'Hearts'):
            ret_utf = "♥"
        elif(str(self.get_suit()) == 'Clubs'):
            ret_utf = "♣"
        elif(str(self.get_suit()) == 'Spades'):
            ret_utf = "♠"
        elif(str(self.get_suit()) == 'Diamonds'):
            ret_utf = "♦"
        else:
            ret_utf = 'null'

        ret_str = f'{self.get_val()} of {self.get_suit()} {ret_utf}' 
        if(self.__error_flag == 1):
            ret_str = "** illegal **"
        return ret_str


    def __str__(self):
        if(str(self.get_suit()) == 'Hearts'):
            ret_utf = "♥"
        elif(str(self.get_suit()) == 'Clubs'):
            ret_utf = "♣"
        elif(str(self.get_suit()) == 'Spades'):
            ret_utf = "♠"
        elif(str(self.get_suit()) == 'Diamonds'):
            ret_utf = "♦"
        else:
            ret_utf = 'null'

        ret_str = f'{self.get_val()} of {self.get_suit()} {ret_utf}' 
        if(self.__error_flag == 1):
            ret_str = "** illegal **"
        return ret_str
        
class Card:
    def __init__(self):
        print("card needs a value and suit")
        self._suit = CardSuit()
        pass


def main():
    # test 1
    # test1 = Card()
    # print(test1.get_val())
    # print(test1.get_suit())
    # print(test1.get_error_flag())
    # print(test1)

    # test 2
    test2 = Card(2, "Bats")
    print(test2.get_val())
    print(test2.get_suit())
    print(test2.get_error_flag())
    print(test2)

    test2.set(2, "Diamonds")
    print(test2.get_val())
    print(test2.get_suit())
    print(test2.get_error_flag())
    print(test2)

    print(Card.valid_card(2, "Diamonds"))


    # test 3
    # test3 = Card("ten", "Hearts")
    # print(test3.get_val())
    # print(test3.get_suit())
    # print(test3.get_error_flag())
    # print(test3)

if __name__ == "__main__":
    main()