#!/usr/bin/env python 
from pprint import pprint
import logging
from logging import info, error
import json
from os import environ
import src.terminal as terminal
import src.api as api
from blessed import Terminal
import time
import configparser
import confire
import sys
import  os
import subprocess

from src.config import configuration
#cfg = configuration()

#print(cfg)

#sys.exit(1)

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

        self.config = configuration()
        self.api = api.Api(api_key=self.config.lichess.api_key)
        self.stream = self.api.stream_board_state(self.game_id)
        self.tui = terminal.GameUi(config=self.config, stream=self.stream, game_id=self.game_id, api=self.api)

    def play(self):
        self.tui.start()
    

game_id = "WGCTQVb7"
game = Game(game_id)
game.play()




#response = api.make_board_move("eFgl5mHdDWHI",LICHESS_API_KEY,"b1c3")


#print(response.text)
##for line in game.iter_lines(decode_unicode=True):
#    if line:
#        event = json.loads(line)
##        pprint(event)
##        print(event["state"]["moves"])
##        time.sleep(0.5)
#        try:
#            #pprint(event)
#            moves = event["moves"]
#        except KeyError:
#            #pprint(event)
#            moves = event["state"]["moves"]
#        finally:
#            terminal.make_moves(moves,last_board)
#           # print(moves)
#lines = stream.iter_lines(decode_unicode=True)
#l1 = next(lines)
#print(l1)
#print(line)
