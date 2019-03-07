from collections import Counter

def coin(player, amount):
    player.plr_status = (Counter(player.plr_status) + Counter(amount))
    return player

def draw(player, amount):
    return(player.draw(amount))

def move(player, what, start, end):
    for what_idx in range(what):
        try:
            player.decks[end] += player.decks[start][what_idx]
            player.decks[start] = player.decks[start][-what_idx]
        except IndexError:
            print("Index for " + start + "is out of range")
    return(player)

def trash(player, what, start):
    move(player=player, what=what, start=start, end='trash')
