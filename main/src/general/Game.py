from main.src.general.Player import Player

class Game:
    """
    Main class for game
    """
    def __init__(self):
        self.game = {
            "players": {},
            "board": {},
            "game_type": "",
        }

    def _add_player(self):
        player_name = input("What is name of the player?")
        while player_name in self.game["players"]:
            print("This name already exists, try different one")
            player_name = input("What is name of the player? Or leave empty to cancel.")
            if player_name == "":
                return None
        self.game["players"][player_name] = {Player()}

    def _remove_player(self):
        player_name = input("What player you want to remove?")
        if player_name in self.game["players"]:
            self.game["players"].pop(player_name)
        else:
            print("No player with that name")

