import src.terminal as terminal
from logging import info
#from blessed import Terminal

BOARD_BACK_ROW_PIECES = ("r","n","b","q","k","b","n","r")
BOARD_ROWS = (1, 2, 3, 4, 5, 6, 7, 8)
BOARD_COLS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
BOARD_POSITIONS = tuple(f"{col}{row}" for row in BOARD_ROWS for col in BOARD_COLS)




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

class Board:
    def __init__(self):
        self.board = []
        for side, front, back in (("white", 2, 1), ("black", 7, 8)):
            for col_i, col in enumerate(BOARD_COLS):
                self.board.append(Piece(side, "p", col=col, row=front))
                self.board.append(Piece(side, BOARD_BACK_ROW_PIECES[col_i], col=col, row=back))

    @staticmethod
    def from_xy(x,y):
        row = (8, 7, 6, 5, 4, 3, 2, 1)
        nx,ny = BOARD_COLS[x],row[y]
        return f"{nx}{ny}"
    def find(self, key):
        """Get the Piece that matches key."""
        for piece in self.board:
            if key == piece.to_pos():
                return piece
        raise KeyError(f"Key Not Found: {key}")

    def index(self, key):
        """Get the index that matches key."""
        for i, piece in enumerate(self.board):
            if key == piece.to_pos():
                return i
        raise KeyError(f"Key Not Found: {key}")

    def __getitem__(self, key):
        """Implement dictionary get functionality"""
        return self.find(key)

    def __setitem__(self, key, value):
        """Implement dictionary set functionality"""
        side, variant = value
        try:
            self.board[self.index(key)] = (Piece(side, variant, pos=key))
        except KeyError:
            self.board.append(Piece(side, variant, pos=key))

    def __repr__(self):
        """How to display Board when printed or logged. """
        return str(self.board)

    def __delitem__(self,key):
        """Implement dictionary del functionality"""
        del self.board[self.index(key)]

    def pop(self,key):
        return self.board.pop(self.index(key))

    def move_piece(self, from_pos, to_pos):
        """Move a piece"""
        # Get index and piece to move
        i, piece = self.index(from_pos), self.find(from_pos)

        # Update coordinates
        piece.from_pos(to_pos)

        # Replace piece
        self.board[i] = piece

    def print_board(self, terminal,player_side=None):
        """Print the game board."""
        # Clear screen and set background
        #print(terminal.red_on_gray + terminal.clear)

        # Loop every possible board position
        for pos in BOARD_POSITIONS:
            try:
                # If positon exists draw the piece.
                p = self.find(pos).draw(terminal,player_side)
            except KeyError:
                # Otherwise draw an empty space
                p = Piece.empty_space(pos).draw(terminal,player_side)

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
        else:
            self.col = None
            self.row = None

    def from_pos(self, pos):
        """Update col, row from input pos"""
        col, row = list(pos)
        self.row = row
        self.col = col

    def to_x(self):
        """Get termial x position from col"""

        return BOARD_COLS.index(self.col)

    def to_y(self):
        """Get termial y position from row"""
        # Reverse tuple and get the value of the row. The -1 is because the row starts at 1 but the tuple at 0.
        return BOARD_ROWS[::-1][int(self.row)-1]-1
    def to_rev_y(self):
        """Get termial y position from row"""
        # Reverse tuple and get the value of the row. The -1 is because the row starts at 1 but the tuple at 0.
        return BOARD_ROWS[int(self.row)-1]-1

    #def to_xy(self):
        #return self.to_x(), self.to_y()

    #def to_yx(self):
        #return self.to_y(), self.to_x()

    def __repr__(self):
        """How to display Piece when printed or logged. """
        return f"{self.col}{self.row}"

    def to_pos(self):
        """Format col and row into a chess position"""
        return f"{self.col}{self.row}"

    def draw(self, terminal,player_side=None):
        """Draw piece"""
        matrix = {
            "p":"p  ",
            "n":"n  ",
            "k":"k  ",
            "q":"q  ",
            "b":"b  ",
            "r":"r  "

        } 
        
        try:
            piece=matrix[self.variant]
        except KeyError:
            piece=".  "
        if player_side == "black":
            x,y = self.to_x(),self.to_rev_y()
        else:
            x,y = self.to_x(),self.to_y()

        with terminal.location(x,y):
            if self.side == "white":
                print(terminal.aquamarine3(piece))
                # springgreen palegreen gray white 
            elif self.side == "black":
                print(terminal.seagreen(piece))
                # mediumseagreen darkgreen black
            else:
                print(piece)
                    

    @staticmethod
    def empty_space(pos):
        """Create a piece that is empty"""
        return Piece(None, None, pos=pos)

#def xy_to_chess_pos(x,y):
    #info("inside chess pos" )
    #info((x,y))
    #matrix = {"x": 
    #        {
    #            "0":"a",
    #            "1":"b",
    #            "2":"c",
    #            "3":"d",
    #            "4":"e",
    #            "5":"f",
    #            "6":"g",
    #            "7":"h"
    #            },
    #        "y":{

    #            "7":"1",
    #            "6":"2",
    #            "5":"3",
    #            "4":"4",
    #            "3":"5",
    #            "2":"6",
    #            "1":"7",
    #            "0":"8"
    #            }
    #        }

    #nx,ny = (matrix["x"][str(x)], matrix["y"][str(y)])
    #info((nx,ny))
    #return f"{nx}{ny}"
