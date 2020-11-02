from __future__ import annotations
import random
from typing import Dict, List, Union, Optional

from Errors import EmptyDeckError
from main.src.card.Card import Card


class Deck:
    """Class for all types of decks"""
    def __init__(self, name: str, cards_dict: Dict[Card, int], preshuffle=True):
        self.__name__ = name
        self.deck = self.unpack_deck(cards_dict)
        if preshuffle:
            random.shuffle(self.deck)

    @staticmethod
    def unpack_deck(dict_deck):
        assert isinstance(dict_deck, dict)
        deck = []
        for key, value in dict_deck.items():
            deck.extend([key]*value)
        return deck

    def draw(self, num_of_cards: Optional[int], not_enough_cards_error=True):
        if num_of_cards is None:
            to_return = self.deck
            self.deck = []
            return to_return
        elif len(self.deck) > num_of_cards:
            to_return = self.deck[-num_of_cards:]
            self.deck = self.deck[:num_of_cards]
            return to_return
        elif not_enough_cards_error:
            raise EmptyDeckError
        else:
            to_return = self.deck
            self.deck = []
            return to_return

    def look(self, num_of_cards: int, not_enough_cards_error=True) -> List[Card]:
        if len(self.deck) >= num_of_cards:
            return self.deck[-num_of_cards:]
        elif not_enough_cards_error:
            raise EmptyDeckError
        else:
            return self.deck

    def add_cards(self, cards_dict: Union[Deck, List[Card], Dict[Card, int]], preshuffle=True) -> None:
        if isinstance(cards_dict, dict):
            new_cards = self.unpack_deck(cards_dict)
        elif isinstance(cards_dict, Deck):
            new_cards = cards_dict.deck
        elif isinstance(cards_dict, list):
            new_cards = cards_dict
        else:
            raise TypeError
        if preshuffle:
            random.shuffle(new_cards)
        self.deck = new_cards + self.deck
