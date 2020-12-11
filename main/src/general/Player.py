from __future__ import annotations
import random
from copy import deepcopy
from typing import List, Optional

from Errors import EmptyDeckError
from main.src.general.Deck import Deck


class Player:

    def __init__(self, name: str, decks: List[Deck], hand_size: int = 5):
        """ possible decks:
        "draw": [],
        "used": [],
        "discard": [],
        "bought": [],
        "hand": [],
        "trash": [],
        "duration": [],
        "mat": [],
        """
        self.__name__ = name
        self.hand_size = hand_size
        self.decks = {}
        for deck in decks:
            deck_name = deck.__name__
            self.decks[deck_name] = deck
        self.current_status = {
            "current_buy": 0,
            "current_coin": 0,
            "current_action": 0,
            "current_player": False,
        }

    def draw(self, deck_from: str, deck_to: str, refill_deck: Optional[str], cards_to_draw: Optional[int]):
        if deck_from not in self.decks:
            raise NameError("Unknown deck " + deck_from)
        elif deck_to not in self.decks:
            raise NameError("Unknown deck " + deck_to)
        elif refill_deck is not None and refill_deck not in self.decks:
            raise NameError("Unknown deck " + refill_deck)
        try:
            drawn_cards = self.decks[deck_from].draw(cards_to_draw)
            self.decks[deck_to].add_cards(drawn_cards, preshuffle=False)
        except EmptyDeckError:
            try:
                self.decks[deck_from].add_cards(self.decks[refill_deck])
                drawn_cards = self.decks[deck_from].draw(cards_to_draw, not_enough_cards_error=False)
                self.decks[deck_to].add_cards(drawn_cards, preshuffle=False)
            except EmptyDeckError:
                pass

    def clean_up(self, deck_from: str, deck_to: str):
        if deck_from not in self:
            raise NameError("Unknown deck " + deck_from)
        elif deck_to not in self:
            raise NameError("Unknown deck " + deck_to)
        drawn_cards = self.decks[deck_from].draw()
        self.decks[deck_to].add_cards(drawn_cards, preshuffle=False)

    def buy(self, what: Deck, where: Deck):
        try:
            card_to_be_bought = what.look(num_of_cards=1, not_enough_cards_error=True)
        except EmptyDeckError:
            return None
        self.current_status, buy_ok = card_to_be_bought[0].buy(self)
        if buy_ok is not None:
            what.draw(num_of_cards=1, not_enough_cards_error=True)
        where.add_cards(card_to_be_bought, preshuffle=False)


class PlayerGenericAction:
    """
    Actions for player
    """
    def __init__(self, player: Player):
        self.player = Player


class CardSpecificAction:
    @classmethod
    def draw(cls, player: Player, **kwargs):
        player.draw(**kwargs)

    @classmethod
    def add_coin(cls, player: Player, number: int = 1):
        player.current_status["current_coin"] += number

    @classmethod
    def add_buy(cls, player: Player, number: int = 1):
        player.current_status["current_buy"] += number

    @classmethod
    def add_action(cls, player: Player, number: int = 1):
        player.current_status["current_action"] += number


    ### DEPRECATED ###
    """
    def cleanup(self,
                discard_hand=True,
                discard_used=True,
                discard_bought=True,
                global_trash=True):
        if discard_hand and 'hand' in self.decks.keys():
            self.decks['discard'] += self.decks['hand']
            self.decks['hand'] = []
        if discard_used and 'used' in self.decks.keys():
            self.decks['discard'] += self.decks['used']
            self.decks['used'] = []
        if discard_bought and 'bought' in self.decks.keys():
            self.decks['discard'] += self.decks['bought']
            self.decks['bought'] = []
        if global_trash and 'trash' in self.decks.keys():
            # define global variable game
            # game.decks['trash'] += self.decks['trash']
            self.decks['trash'] = []
        return self

    def play(self,
             card):
        self = card.play(self)

    def print_status(self):
        print("Player has following cards in hand:")
        print(self.decks['hand'])
        print("There are {} card(s) in draw pile. There are {} card(s) in discard".format(
            len(self.decks['draw']),
            len(self.decks['discard'])))
        return None
    """
