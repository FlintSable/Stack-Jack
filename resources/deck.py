"""
This class will represent a deck of cards
"""
from card import Card, Node


# maybe implement a queue with a linked list
# class LinkedList:
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
            return_str += str(node)
            node = node.next
        return return_str

class Deck:
    def __init__(Stack):
        # instantiage whole deck of cards
        # 52 cards in a deck = 52 Nodes with different suits

        # 13 cards in a suit
        # create 4 lists of 13 cards, jumble them
        # push them one list at a time to the stack
        # then deck will be full

        pass

    def gen_hearts():
        pass
    def gen_diamonds():
        pass
    def gen_spades():
        pass
    def gen_clubs():
        pass



def main():
    pass


if __name__ == "__main__":
    main()