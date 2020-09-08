class Card:
    """ Class for generic cards"""
    def __init__(self, card_name, card_fcn, card_text, card_cost, card_cost_buys=1):
        self.card_name = card_name
        self.card_fcn = card_fcn
        self.card_text = card_text
        self.card_cost = card_cost
        self.card_cost_buys = card_cost_buys

    def print(self):
        print(self.card_name + "(" + str(self.card_cost) + "$)")

    def print_all(self):
        print("Card name: {}\n".format(self.card_name),
              "Card text: {}\n".format(self.card_text),
              "Card fucntion: {}".format(self.card_fcn))

class CardGenericAction:
    """
    Actions for generic card
    """
    def __init__(self, card):
        self.card = card

    def buy(self):

