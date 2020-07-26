import src.terminal as terminal
#from blessed import Terminal

#term = Terminal()
BOARD_BACK_ROW_PIECES = ("r","n","b","q","k","b","n","r")
BOARD_ROWS = (1, 2, 3, 4, 5, 6, 7, 8)
BOARD_COLS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
BOARD_POSITIONS = tuple(f"{col}{row}" for row in BOARD_ROWS for col in BOARD_COLS)
#print(BOARD_POSITIONS)


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


def step_moves(current_move_list, new_move_list):
    new_statemaps =[]
    if current_move_list == new_move_list:
        pass
    elif new_move_list.startswith(current_move_list):
        statemap = Board()
        for move in new_move_list.split():
            from_pos = move[0:2]
            to_pos = move[2:4]

            statemap.move_piece(from_pos, to_pos)
            new_statemaps.append(statemap)
    return new_statemaps


def row_range():
    """  generates row numbers """
    for i in range (1,8+1):
        yield i

def col_range():
    for c in range(ord("a"), ord("h")+1):
        yield chr(c)

class Board:
    def __init__(self):
        self.board = []
        for side, front, back in (("white", 2, 1), ("black", 7, 8)):
            for col_i, col in enumerate(BOARD_COLS):
                self.board.append(Piece(side, "p", col, front))
                self.board.append(Piece(side, BOARD_BACK_ROW_PIECES[col_i], col, back))

    def find(self, key):
        for piece in self.board:
            if key == piece.to_pos():
                return piece
        
        raise KeyError(f"Index Not Found: {key} ")

    def index(self, key):
        #print(self.board)
        for i, piece in enumerate(self.board):
            #print(key, piece.to_pos())
            if key == piece.to_pos():
                return i
        raise KeyError(f"Index Not Found: {key} ")

    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, value):
        side, variant = value
        try:
            i = self.index(key)
            self.board.append(Piece(side, variant, pos=key))
        except KeyError:
            self.board.append(Piece(side, variant, pos=key))

    def __repr__(self):
        return str(self.board)

    def __delitem__(self,key):
        del self.board[self.index(key)]

    def pop(self,key):
        return self.board.pop(self.index(key))

    def move_piece(self, from_pos, to_pos):
        i, piece = self.index(from_pos), self.find(from_pos)
        #print(self.board)
        piece.from_pos(to_pos)
        self.board.append(piece)
        del self.board[i]

    def print_board(self, terminal):

        print(terminal.white_on_black + terminal.clear)
        for pos in BOARD_POSITIONS:
            try:
                p = self.find(pos)
                #print(f"pos: {pos} p: {p}")
                p.draw(terminal)
                #self.find(pos).draw(terminal)
                #print(pos, piece.variant)
            except KeyError:
                p = Piece.empty_space(pos)
                #print(f"pos: {pos} p: {p}")
                p.draw(terminal)
                #print(pos, ".")
                #print("ERRORED KEYS LOL")
                

    def draw(self):
        pass 
        #for i



 


class Piece:
    def __init__(self,side, variant, col=None, row=None, pos=None):
        self.side = side
        self.variant= variant
        if col and row:
            self.col = col
            self.row = row
        elif pos:
            self.col = pos[0]
            self.row = pos[1]
        #elif x and y:
        #    self.col = None
        #    self.row = None
        #elif yx:
        #    self.col = None
        #    self.row = None
        else:
            self.col = None
            self.row = None



    def from_pos(self, pos):
        col, row = list(pos)
        self.row = row
        self.col = col




    def to_x(self):
        return BOARD_COLS.index(self.col)

    def to_y(self):
        return BOARD_ROWS[::-1][int(self.row)-1]

    def to_xy(self):
        return self.to_x(), self.to_y()

    def to_yx(self):
        return self.to_y(), self.to_x()

    def __repr__(self):
        return f"{self.col}{self.row} -> {self.side} -> {self.variant}\n"

    def to_pos(self):
        return f"{self.col}{self.row}"
    def draw(self, terminal):
        matrix = {
            "p":"p  ",
            "n":"n  ",
            "k":"k  ",
            "q":"q  ",
            "b":"b  ",
            "r":"r  "

        } 
        try:
            piece = matrix[self.variant]
        except KeyError:
            piece=".  "

        with terminal.location(self.to_x(),self.to_y()):
            print(piece)
        #print(self.to_pos(), piece)

    @staticmethod
    def empty_space(pos):
        return Piece(None, None, pos=pos)


        
#def new_board():
#    board = {
#            }
#    for side,front_row, back_row in [("black",7,8),("white",2,1)]:
#        for pos in row_positions(front_row):
#            board[pos] = Piece(side,"p", pos)
#        back_row_pieces = ["r","n","b","q","k","b","n","r"]
#        for piece,pos in zip(back_row_pieces,row_positions(back_row)):
#            board[pos] = Piece(side,piece)
#
#    return board
