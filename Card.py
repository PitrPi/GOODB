from Errors import NotPlayableError

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

    def buy(self, plr_status):
        if (plr_status.crnt_buy > self.card_cost_buys or
                plr_status.crnt_money < self.card_cost):
            if debug:
                print("Player cannot buy card")
            return -1
        else:
            plr_status.crnt_buy -= self.card_cost_buys
            plr_status.crnt_money -= self.card_cost
            return(self, plr_status)

    def play(self, player):
        """ This method should cycle through card functions and trigger them
        When action is not possible trigger fallback
        (that can be ignore action or end evaluation)
        """
        for fcn_idx in range(self.card_fcn):
            try:
                self.card_fcn[fcn_idx](player)
            except NotPlayableError:
                print("Not playable")


######################
#### UNIT TESTING ####
# ######################
#
# card1 = Card("Test", "Gives 1$", "This is basic train", 4)
# card1.print_all()
# card1.print()