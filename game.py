from pprint import pprint
import logging
from logging import info, error
import json
from os import environ
import src.terminal as terminal
import src.api as api
from blessed import Terminal
import time
#test_moves =  'e2e3 e7e5 d2d3 c7c5 c2c3 g8f6 f2f3 b8c6 f3f4 e5f4'
logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
LICHESS_API_KEY = environ["LICHESS_API_KEY"]
live_game_id = "iLmvOgQ4"
stream = api.stream_board_state(live_game_id, LICHESS_API_KEY)
info("test")

#response = api.make_board_move("eFgl5mHdDWHI",LICHESS_API_KEY,"b1c3")
terminal.play_game(stream)


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
lines = stream.iter_lines(decode_unicode=True)
l1 = next(lines)
print(l1)
#print(line)
