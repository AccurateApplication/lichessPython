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
def convert_pos(x,y):
    pass

#def convert_pos(position):
#    if len(position) == 2:
#        x,y = position[0],position[1]
#        matrix = {"x": 
#                {
#                    "a":0,
#                    "b":1 ,
#                    "c":2 ,
#                    "d":3 ,
#                    "e":4 ,
#                    "f":5 ,
#                    "g":6 ,
#                    "h":7 
#                    },
#                "y":{
#
#                    "1":7 ,
#                    "2":6 ,
#                    "3":5 ,
#                    "4":4 ,
#                    "5":3 ,
#                    "6":2 ,
#                    "7":1 ,
#                    "8":0
#                    }
#                }
#        return matrix["x"][x], matrix["y"][y]


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
    print(from_pos,state)
    piece = state.pop(from_pos)
    state[to_pos]=piece
    return state

def row_range():
    """  generates row numbers """
    for i in range (1,8+1):
        yield i

def col_range():
    for c in range(ord("a"), ord("h")+1):
        yield chr(c)

def pos(col,row):
    return f"{col}{row}"

def row_positions(row):
    return [Position(col,row) for col in col_range()]

def col_positions(col):
    return [Position(col,row) for row in row_range()]

def empty_board():
    return {Position(col,row):None for row in row_range() for col in col_range()}
class Position:
    def __init__(self,col,row,piece=None):
        self.col=col
        self.row=row
        self.piece=piece
    def __repr__(self):
        return f"{self.col}{self.row}"
class Board:
    def __init__(self):
        self.position = Board.setup()

        pass
    def __get__(self,instance,owner):
        print("hello")
        for pos in self.position:
            if pos == self.value:
                return pos


    @staticmethod
    def setup():
        return [Position("a","2",Piece("white","b")),Position("a","3",Piece("black","b"))]
        pass

class Piece:
    def __init__(self,side,variant):
        # variant == "piece"
        self.side = side
        self.variant= variant
    def __print__(self):
        return f"{self.variant}={self.side}"

def new_board():
    board = {
            }
    for side,front_row, back_row in [("black",7,8),("white",2,1)]:
        for pos in row_positions(front_row):
            board[pos] = Piece(side,"p")
        back_row_pieces = ["r","n","b","q","k","b","n","r"]
        for piece,pos in zip(back_row_pieces,row_positions(back_row)):
            board[pos] = Piece(side,piece)

    return board
