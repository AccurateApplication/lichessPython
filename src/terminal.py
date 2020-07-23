from pprint import pprint
import src.api as api
from logging import info
import _thread
import json
from blessed import Terminal
import time
import sys
term = Terminal()

live_game_id = "iLmvOgQ4"

def echo(text):

    """Python 2 version of print(end='', flush=True)."""
    sys.stdout.write(u'{0}'.format(text))
    sys.stdout.flush()

def draw_piece(position, piece):
    x,y = convert_pos(position)
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

def yx_to_chess_pos(pos):
    y,x = pos
    matrix = {"x": 
            {
                "0":"a",
                "1":"b",
                "2":"c",
                "3":"d",
                "4":"e",
                "5":"f",
                "6":"g",
                "7":"h"
                },
            "y":{

                "7":"1",
                "6":"2",
                "5":"3",
                "4":"4",
                "3":"5",
                "2":"6",
                "1":"7",
                "0":"8"
                }
            }
    nx,ny = (matrix["x"][str(x)], matrix["y"][str(y)])
    return f"{nx}{ny}"
def convert_pos(position):
    if len(position) == 2:
        x,y = position[0],position[1]
        matrix = {"x": 
                {
                    "a":0,
                    "b":1 ,
                    "c":2 ,
                    "d":3 ,
                    "e":4 ,
                    "f":5 ,
                    "g":6 ,
                    "h":7 
                    },
                "y":{

                    "1":7 ,
                    "2":6 ,
                    "3":5 ,
                    "4":4 ,
                    "5":3 ,
                    "6":2 ,
                    "7":1 ,
                    "8":0
                    }
                }
        return matrix["x"][x], matrix["y"][y]

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def new_board():
    state_map = {
        f"{x}{y}":"" for x in char_range('a', 'h')
        for y in range(1,9)
        }
    start_pos = {
            "white":{
                "a1": "r",
                "b1": "n",
                "c1": "b",
                "d1": "q",
                "e1": "k",
                "f1": "b",
                "g1": "n",
                "h1": "r",
                "a2": "p",
                "b2": "p",
                "c2": "p",
                "d2": "p",
                "e2": "p",
                "f2": "p",
                "g2": "p",
                "h2": "p"
                },
            "black":{
                "a8": "r",
                "b8": "n",
                "c8": "b",
                "d8": "q",
                "e8": "k",
                "f8": "b",
                "g8": "n",
                "h8": "r",
                "a7": "p",
                "b7": "p",
                "c7": "p",
                "d7": "p",
                "e7": "p",
                "f7": "p",
                "g7": "p",
                "h7": "p"
                }
            }
    for player in ["white","black"]:
        for pos,piece in start_pos[player].items():
            #print(pos,piece)
            #print(state_map[pos])
            state_map[pos]=piece
    return state_map

def print_board(state):
    print(term.black_on_olivedrab4 + term.clear)
    for pos,piece in state.items():
        if piece == "":
             piece = "."
        draw_piece(pos,piece) 

def move_piece(state,from_pos,to_pos):
    new_state = state
    piece = new_state[from_pos]
    new_state[from_pos]=""
    new_state[to_pos]=piece
    return new_state

def handle_player():
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
                #echo(term.move_yx(3, 3))

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
                from_pos = yx_to_chess_pos(term.get_location(timeout=0.1))
            elif val == u"c":
                to_pos = yx_to_chess_pos(term.get_location(timeout=0.1))
            elif val == u"m":
                move = f"{from_pos}{to_pos}"
                r = api.make_board_move(live_game_id,move)
                info((r.text,r.status_code))
                info(move)
            info("wait now idiot!!!")
def play_game(stream):

    with term.cbreak():
        from_pos = 0
        to_pos = 0
        #new_moves =  'e2e3 e7e5 d2d3 c7c5 c2c3 g8f6 f2f3 b8c6 f3f4 e5f4'
        #latest_moves =  'e2e3 e7e5 d2d3 c7c5 c2c3 g8f6 f2f3 b8c6 f3f4 e5f4'
        #c_x,c_y = (0,0)
        latest_moves = ""
        last_board = new_board()
        _thread.start_new_thread(handle_player,())
        for line in stream.iter_lines(decode_unicode=True):
            if line:
                info("start of upadiasdu")
                event = json.loads(line)
        #        pprint(event)
        #        print(event["state"]["moves"])
        #        time.sleep(0.5)
                try:
                    #pprint(event)
                    new_moves = event["moves"]
                except KeyError:
                    #pprint(event)
                    new_moves = event["state"]["moves"]
                finally:
                    #make_moves(newmoves,last_board)
                    new_statemaps = step_moves(latest_moves, new_moves)
                    for statemap in new_statemaps:
                        print_board(statemap)

                    info("end of board updtuaudsaijd")
                #info("click now idiot!!!")
                #val = term.inkey(timeout=0.1)
                #if val == u"j":
                #    info("down")
                #    #term.move_xy(x,y-1)
                #    echo(term.move_down(1))
                #    #echo(term.move_yvx(3, 3))

                #elif val == u"k":
                #    echo(term.move_up(1))
                #    info("up is the only way")
                #elif val == u"l":
                #    echo(term.move_right(1))
                #    info("rightis the only way")
                #elif val == u"h":
                #    echo(term.move_left(1))
                #    info("leftis the only way")
                #elif val == u"x":
                #    from_pos = term.get_location(timeout=0.1)
                #elif val == u"c":
                #    to_pos = term.get_location(timeout=0.1)

                #info(f"{from_pos},{to_pos}")
                ##info(f"{val.code},{val}")
                #info("wait now idiot!!!")

def step_moves(current_move_list, new_move_list):
    new_statemaps =[]
    if current_move_list == new_move_list:
        pass
    elif new_move_list.startswith(current_move_list):
        statemap = new_board()
        for move in new_move_list.split():
            from_pos = move[0:2]
            to_pos = move[2:4]
            #print(from_pos, to_pos)

            statemap = move_piece(statemap,from_pos,to_pos)
            new_statemaps.append(statemap)
    return new_statemaps

def make_moves(move_list,current_state):
    statemap = new_board()
    for move in move_list.split():
        from_pos = move[0:2]
        to_pos = move[2:4]
        #print(from_pos, to_pos)

        statemap = move_piece(statemap,from_pos,to_pos)
        if statemap != current_state:
            print_board(statemap)
    #change_board = statemap.copy()
    #print_board(change_board)
    #time.sleep(5)



#print(term.home + term.clear + term.move_y(term.height // 2))
#print(term.black_on_darkkhaki(term.center('press any key to continue.')))
#
#with term.cbreak(), term.hidden_cursor():
#    inp = term.inkey()
#
#print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))
