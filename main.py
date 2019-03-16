debug = True
import random
import Run

def main():
    players = Run.setup_game()
    random.shuffle(players)
    Run.play(players)


if __name__ == "__main__":
    # execute only if run as script
    main()

