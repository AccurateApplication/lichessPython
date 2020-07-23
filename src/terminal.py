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
        self.stream = stream
        self.api = api
        self.game_id = game_id

    def handle_player(self):
        from_pos = 0
        to_pos = 0
        while True :
            with term.cbreak():
                info("click now idiot!!!")
                val = term.inkey(timeout=3)
                if val == u"j":
                    info("down")
                    #term.move_xy(x,y-1)
                    echo(term.move_down(1))
    
                elif val == u"k":
                    echo(term.move_up(1))
                    info("up is the only way")
                elif val == u"l":
                    echo(term.move_right(1))
                    info("rightis the only way")
                elif val == u"h":
                    echo(term.move_left(1))
                    info("leftis the only way")
                elif val == u"x":
                    from_pos = chess.yx_to_chess_pos(term.get_location(timeout=0.1))
                elif val == u"c":
                    to_pos = chess.yx_to_chess_pos(term.get_location(timeout=0.1))
                elif val == u"m":
                    move = f"{from_pos}{to_pos}"
                    r = self.api.make_board_move(self.game_id,move)
                    info((r.text,r.status_code))
                    info(move)
                info("wait now idiot!!!")
    def start(self):
    
        with term.cbreak():
            from_pos = 0
            to_pos = 0
            #new_moves =  'e2e3 e7e5 d2d3 c7c5 c2c3 g8f6 f2f3 b8c6 f3f4 e5f4'
            #latest_moves =  'e2e3 e7e5 d2d3 c7c5 c2c3 g8f6 f2f3 b8c6 f3f4 e5f4'
            #c_x,c_y = (0,0)
            latest_moves = ""
            last_board = chess.new_board()
            _thread.start_new_thread(self.handle_player,())
            for line in self.stream.iter_lines(decode_unicode=True):
                if line:
                    info("start of upadiasdu")
                    event = json.loads(line)
            #        pprint(event)
            #        print(event["state"]["moves"])
            #        time.sleep(0.5)
                    try:
                        new_moves = event["moves"]
                    except KeyError:
                        #pprint(event)
                        new_moves = event["state"]["moves"]
                    finally:
                        new_statemaps = chess.step_moves(latest_moves, new_moves)
                        for statemap in new_statemaps:
                            print_board(statemap)
    

def echo(text):

    """Python 2 version of print(end='', flush=True)."""
    sys.stdout.write(u'{0}'.format(text))
    sys.stdout.flush()

def draw_piece(position, piece):
    x,y = chess.convert_pos(position)
    matrix = {
            "p":"♙  ",
            "n":"♘  ",
            "k":"♔  ",
            "q":"♕  ",
            "b":"♗  ",
            "r":"♖  "

            } 
    try:
        piece = matrix[piece]
    except KeyError:
        piece=".  "

    with term.location(x,y):
        print(piece)



def print_board(state):
    print(term.black_on_olivedrab4 + term.clear)
    for pos,piece in state.items():
        if piece == "":
             piece = "."
        draw_piece(pos,piece) 



def make_moves(move_list,current_state):
    statemap = chess.new_board()
    for move in move_list.split():
        from_pos = move[0:2]
        to_pos = move[2:4]

        statemap = chess.move_piece(statemap,from_pos,to_pos)
        if statemap != current_state:
            print_board(statemap)

