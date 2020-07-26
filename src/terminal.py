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


def draw():
    pass

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
            #with term.cbreak():
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
    
        with  term.fullscreen(),term.cbreak():
            from_pos = 0
            to_pos = 0
            latest_moves = ""
            last_board = chess.Board()
            _thread.start_new_thread(self.handle_player,())
            for line in self.stream.iter_lines(decode_unicode=True):
                if line:
                    
                    event = json.loads(line)
                    #print(event)
                    try:
                        new_moves = event["moves"]
                        new_statemaps = chess.step_moves(latest_moves, new_moves)
                    except KeyError:
                        #pprint(event)
                        new_moves = event["state"]["moves"]
                        #latest_moves = chess.new_board()
                        new_statemaps = chess.step_moves(latest_moves, new_moves)

                    for statemap in new_statemaps:
                        statemap.print_board(term)
                        #print_board(statemap)

def echo(text):

    """Python 2 version of print(end='', flush=True)."""
    sys.stdout.write(u'{0}'.format(text))
    sys.stdout.flush()

#
            #} 
#def draw_piece(position, piece):
#    x,y = chess.convert_pos(position)
#    matrix = {
#            "p":"p  ",
#            "n":"n  ",
#            "k":"k  ",
#            "q":"q  ",
#            "b":"b  ",
#            "r":"r  "
#
#            } 
#    try:
#        piece = matrix[piece.variant]
#    except KeyError:
#        piece=".  "

   # with term.location(x,y):
   #     print(piece)
def print_board(state):
    print(term.white_on_black + term.clear)
    for piece in state.board:
        draw_piece(piece.to_pos(),piece.variant) 




