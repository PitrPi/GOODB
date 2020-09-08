import random
from copy import deepcopy

class Player:
    def __init__(self, decks=None, clean_ups=None):
        if decks is None:
            decks = {
                "draw": [],
                "used": [],
                "discard": [],
                "bought": [],
                "hand": [],
                "trash": [],
                "duration": [],
                "mat": [],
            }  # Set up default decks
        self.decks = decks
        if clean_ups is None:
            clean_ups = ["used", "bought", "hand"]
        self.player_status = {

        }

    def draw(self, cards_to_draw):
        while cards_to_draw <= 0:
            if self.decks["draw"]:
                self.decks["hand"].append(self.decks["draw"].pop())
                cards_to_draw -= 1
            else:
                if self.decks["discard"]:
                    random.shuffle(self.decks["discard"])
                    self.decks["draw"] = deepcopy(self.decks["discard"])
                    self.decks["discard"] = []
                else:
                    cards_to_draw = 0
