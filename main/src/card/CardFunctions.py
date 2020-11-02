from collections import counter


class CardFunctions:
    def move_card(self, origin, tagret):
        pass

    def draw(self):
        self.move_card(origin="draw", target="hand")

    def coin(player, amount):
        player.plr_status = (counter(player.plr_status) + counter(amount))
        return player

    def draw(player, amount):
        return(player.draw(amount))

    def move(player, what, start, end):
        for what_idx in range(what):
            try:
                player.decks[end] += player.decks[start][what_idx]
                player.decks[start] = player.decks[start][-what_idx]
            except indexerror:
                print("index for " + start + "is out of range")
        return(player)

    def trash(player, what, start):
        move(player=player, what=what, start=start, end='trash')
