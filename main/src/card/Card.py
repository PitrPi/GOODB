from __future__ import annotations

from typing import List

from Errors import NotPlayableError
from main.config import CONFIG

debug = CONFIG["debug"]

class CardGenericAction:
    """
    Actions for generic card
    +coin, +card, +action, ...
    """



class Card:
    """ Class for generic cards"""
    def __init__(self,
                 card_name: str,
                 card_fcn: List[CardSpecificAction],
                 card_text: str,
                 card_cost: int,
                 card_cost_buys: int = 1):
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
              "Card function: {}".format(", ".join([x.__name__ for x in self.card_fcn])))

    def buy(self, plr):
        if (plr.current_status.current_buy < self.card_cost_buys or
                plr.current_status.current_coin < self.card_cost):
            if debug:
                print("Player cannot buy card")
            return plr, None
        else:
            plr.current_status.current_buy -= self.card_cost_buys
            plr.current_status.current_coin -= self.card_cost
            return plr.current_status, self

    def play(self, player):
        """ This method should cycle through card functions and trigger them
        When action is not possible trigger fallback
        (that can be ignore action or end evaluation)
        """
        for fcn in self.card_fcn:
            try:
                fcn(player)
            except NotPlayableError:
                print("Not playable")





if __name__ == '__main__':

    copper = Card("Copper", CardSpecificAction.add_coin(p1), "Adds $1", 1)