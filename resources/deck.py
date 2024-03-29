"""
This class will represent a deck of cards
"""
import random
from card import Card, CardSuit, CardValue, Node


#     def __init__(self):
#         self.head = Node()
class Stack:
    def __init__(self):
        self.top = None
    def push(self, node):
        node.next = self.top
        self.top = node
    def pop(self):
        node = self.top
        self.top = self.top.next
        node.next = None
        return node
    def __str__(self):
        node = self.top
        return_str = ""
        while node is not None:
            # return_str += str(node.data.suit)
            return_str += str(node)
            node = node.next

        return return_str

class Deck(Stack):
    def __init__(self):
        Stack.__init__(self)
        # n1 = Node(Card(CardSuit.SPADES, CardValue.FIVE))
        # n2 = Node(Card(CardSuit.SPADES, CardValue.FIVE))

        # instantiage whole deck of cards
        # 52 cards in a deck = 52 Nodes with different suits
        cardvalues = [CardValue.ACE, 
                        CardValue.TWO, 
                        CardValue.THREE,
                        CardValue.FOUR,
                        CardValue.FIVE,
                        CardValue.SIX,
                        CardValue.SEVEN,
                        CardValue.EIGHT,
                        CardValue.NINE,
                        CardValue.TEN,
                        CardValue.JACK,
                        CardValue.QUEEN,
                        CardValue.KING]
        spade_cards = [Node(Card(x, CardSuit.SPADES, x.name)) for x in cardvalues]
        heart_cards = [Node(Card(x, CardSuit.HEARTS, x.name)) for x in cardvalues]
        diamond_cards = [Node(Card(x, CardSuit.DIAMONDS, x.name)) for x in cardvalues]
        clubs_cards = [Node(Card(x, CardSuit.CLUBS, x.name)) for x in cardvalues]
        predeck = spade_cards + heart_cards + diamond_cards + clubs_cards

        # for x in predeck:
        #     print(x.data.card)

        # print("putting cards into deck: ")
        for x in random.sample(predeck, len(predeck)):
            self.push(x)
            # print(x.data)
        
        # just takeing a look at the data, data is still in stack
        # print("top: ")
        # print(self.top.data.card)
        # print("next: ")
        # print(self.top.next.data.card)


    def gen_hearts():
        pass
    def gen_diamonds():
        pass
    def gen_spades():
        pass
    def gen_clubs():
        pass



def main():
    
    new_deck = Deck()

    # prints stack deck, not legible
    # print("deck: ", new_deck)


if __name__ == "__main__":
    main()