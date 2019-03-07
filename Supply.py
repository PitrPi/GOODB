# import Card

class Supply
    """
    This method should generate set-up for the game.
    Decks of available cards and track their number
    """
    def __init__(self, cards, cnt):
        self.cards_list = dict(zip(cards, cnt))

    def buy(self, card, plr_status):
        if self.cards_list[card] <= 0:
            if debug:
                print("No more cards in supply")
            return -1
        else:
           # bought_pile, plr_status
           return(card.buy(plr_status))
