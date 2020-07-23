#!/usr/bin/env python 
import sys
from src.game import Game


if __name__ == "__main__":
    try:
        game_id = sys.argv[1]
    except IndexError:
        print("ERROR! No game id.")
        print("Usage:\ngame.py <game_id>")
        sys.exit(1)

    game = Game(game_id)
    game.play()
    
    
