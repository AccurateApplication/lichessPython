from pprint import pprint
#import src.api as api
from logging import info
import _thread
import json
from blessed import Terminal
import time
import src.chess as chess
import sys
term = Terminal()

class GameUi:
    def __init__(self, config, stream, game_id, api):
        self.config = config
        self.user = api.get_profile().json()["id"]

        self.player_side = None
        self.stream = stream
        self.api = api
        self.game_id = game_id
        self.current_board = None

        self.x = 0
        self.y = 0
    def draw_cursor(self):
        info("drawing cursor")
        echo(term.move_xy(self.x,self.y))
    def up(self):
        self.y -= 1
        self.draw_cursor()
    def down(self):
        self.y += 1
        self.draw_cursor()
    def right(self):
        self.x += 1
        self.draw_cursor()
    def left(self):
        self.x -= 1
        self.draw_cursor()
    def handle_player(self):
        from_pos = 0
        to_pos = 0
        while True :
            #with term.cbreak():

            val = term.inkey(timeout=1)
            info((self.x,self.y))
            if val == u"j":
                info("down")
                self.down()
            elif val == u"k":
                info("up is the only way")
                self.up()
            elif val == u"l":
                info("rightis the only way")
                self.right()
            elif val == u"h":
                info("leftis the only way")
                self.left()
            elif val == u"x":
                x,y = self.x,self.y
                #from_pos = chess.xy_to_chess_pos(x,y)
                from_pos = chess.Board.from_xy(x,y)
                #from_pos = chess.xy_to_chess_pos(x,y)
            elif val == u"c":
                x,y = self.x,self.y
                to_pos = chess.Board.from_xy(x,y)
                #to_pos = chess.xy_to_chess_pos(x,y)
            elif val == u"m":
                move = f"{from_pos}{to_pos}"
                info(move)
                r = self.api.make_board_move(self.game_id,move)
                info((r.text,r.status_code))
                info(move)
    def start(self):
        with  term.fullscreen(),term.cbreak():
            print(term.red_on_gainsboro + term.clear)
            from_pos = 0
            to_pos = 0
            latest_moves = ""
            last_board = chess.Board()
            _thread.start_new_thread(self.handle_player,())
            for line in self.stream.iter_lines(decode_unicode=True):
                if line:
                    event = json.loads(line)
                    info(event)
                    #print(event)
                    try:
                        new_moves = event["moves"]
                        new_statemaps = chess.step_moves(latest_moves, new_moves)
                    except KeyError:
                        # new stream is established here
                        new_moves = event["state"]["moves"]
                        #info(event["white"]["id"])
                        self.player_side = get_user_side(event,self.user)
                        #latest_moves = chess.new_board()
                        new_statemaps = chess.step_moves(latest_moves, new_moves)

                    for statemap in new_statemaps:
                        statemap.print_board(term,self.player_side)
                        self.current_board = statemap
                        self.draw_cursor()
                        #print_board(statemap)

def get_user_side(event,user):
    if "id" in event["white"].keys():
        if user == event["white"]["id"]:
            return "white"

    if "id" in event["black"].keys():
        if user == event["black"]["id"]:
            return "black"

def echo(text):
    """Python 2 version of print(end='', flush=True)."""
    sys.stdout.write(u'{0}'.format(text))
    sys.stdout.flush()

