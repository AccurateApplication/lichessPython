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

def step_moves(current_move_list, new_move_list):
    new_statemaps =[]
    if current_move_list == new_move_list:
        pass
    elif new_move_list.startswith(current_move_list):
        statemap = new_board()
        for move in new_move_list.split():
            from_pos = move[0:2]
            to_pos = move[2:4]

            statemap = move_piece(statemap,from_pos,to_pos)
            new_statemaps.append(statemap)
    return new_statemaps

def move_piece(state,from_pos,to_pos):
    new_state = state
    piece = new_state[from_pos]
    new_state[from_pos]=""
    new_state[to_pos]=piece
    return new_state
