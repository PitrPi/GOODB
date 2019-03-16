import random
debug = True

class Player:
    """ Class for players
    Should init player deck with cards
    and manage player status
    """

    def __init__(self,
                 decks={'draw': {},
                        'used': {},
                        'discard': {},
                        'bought': {},
                        'hand': {},
                        'trash': {}},
                 plr_status = {},
                 cards_to_draw = 5):
        """ this specify players deck
        """

        def unpack_deck(dict_deck):
            assert isinstance(dict_deck, dict)
            deck = []
            for key, value in dict_deck.items():
                deck.extend([key]*value)
            return deck

        self.decks = {}
        for key in decks.keys():
            self.decks[key] = (unpack_deck(decks[key]))
            random.shuffle(self.decks[key])
        if debug:
            print(self.decks)
        self.cards_to_draw = cards_to_draw
        self.plr_status = plr_status

    def draw(self,
             cards_to_draw=None):
        if cards_to_draw is None:
            cards_to_draw = self.cards_to_draw
        if len(self.decks['draw']) >= cards_to_draw:
            self.decks['hand'] += self.decks['draw'][:(cards_to_draw)]
            self.decks['draw'] = self.decks['draw'][(cards_to_draw):]
        else:
            random.shuffle(self.decks['discard'])
            self.decks['draw'] += self.decks['discard']
            self.decks['discard'] = []
            if (len(self.decks['draw']) + len(self.decks['discard'])) >= cards_to_draw:
                self.decks['hand'] += self.decks['draw'][:(cards_to_draw)]
                self.decks['draw'] = self.decks['draw'][(cards_to_draw):]
            else:
                self.decks['hand'] += self.decks['draw']
                self.decks['draw'] = []
        return self

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

######################
#### UNIT TESTING ####
######################
# print('P1: Initial setup')
# player1 = Player(decks={'draw': {'Copper': 7, 'Estate': 3},
#                         'hand': {},
#                         'discard': {}})
# player2 = Player(decks={'draw': {'Normal train': 7, 'Station expanstion': 1, 'Lay rails': 2},
#                         'hand': {},
#                         'discard': {}})
# player1.draw(4)
# print('P1: After drawing 4')
# print(player1.decks)
# player1.draw(4)
# print('P1: After drawing 8')
# print(player1.decks)
# player2.draw(3)
# print('P2: After drawing 3')
# print(player2.decks)
# player1.draw(4)
# print('P1: After drawing 12')
# print(player1.decks)
# player2.draw(5)
# print('P2: After drawing 8')
# print(player2.decks)
# player1.cleanup()
# print('P1: After Cleanup')
# print(player1.decks)

