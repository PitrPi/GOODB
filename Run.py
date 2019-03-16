import Player

def setup_game():
    while True:
        type_of_game = input("What game are we playing or specify starting draw deck")
        if type_of_game == "Dominion":
            print("Nice! That is classic!")
            starting_deck = {'draw': {'Copper': 7, 'Estate': 3},
                             'hand': {},
                             'discard': {}}
            break
        elif type_of_game == "Trains":
            print("Trains!")
            starting_deck = {'draw': {'Normal train': 7, 'Station expansion': 1, 'Lay rails': 2},
                             'hand': {},
                             'discard': {}}
            break
        else:
            try:
                type_of_game['draw']
                starting_deck = type_of_game
                break
            except KeyError:
                print("Cannot find draw deck. Have you provided dictionary with draw as key?")
            except TypeError:
                print("It seems that you did neither provided dictionary as deck nor name of game.")
    while True:
        number_of_players = input("How many players will be playing? (1-6)")
        try:
            number_of_players = int(number_of_players)
        except ValueError:
            print("Please provide number of players.")
            continue
        if int(number_of_players) < 1:
            print("You cannot play with less then 1 player.")
        elif (number_of_players) > 6:
            if input("It is not wise to play with more then 6players. Are you sure you want to proceed? (Y/N)") == 'Y':
                break
        else:
            break
    players = []
    for _ in range(number_of_players):
        player = Player.Player(starting_deck)
        player.draw(5)
        players.append(player)

    return players

def play(players):
    inpt = ""
    print("You start playing, you can quit by pressing 'Q'")
    current_player = 0
    while inpt != "Q":
        players[current_player].print_status()
        inpt = input("What is your next action? (P)lay, (E)nd turn, (B)uy, (D)o effect, (Q)uit")
        if inpt == "P":
            while True:
                subinpt = input("What card you want to play?")
                try:
                    subinpt = int(subinpt)
                    players[current_player].play(players[current_player].decks['draw'][subinpt])
                    break
                except IndexError:
                    print("Card index out of bounds.")
                except ValueError:
                    print("Please provide integer as card index")

        elif inpt == "E":
            print("Ending turn")
            players[current_player] = players[current_player].cleanup()
            players[current_player] = players[current_player].draw(5)
            current_player += 1
            current_player %= len(players)
            print("Currently playing Player {}".format(current_player))
        elif inpt == "B":
            continue
        elif inpt == "Q":
            break
        else:
            print("Unknown action, please try again")