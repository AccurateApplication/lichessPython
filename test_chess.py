import src.chess as ch
import src.terminal as term
from pprint import pprint as pp

bd = {
    "h1": None
}
b = ch.Board()
#pp(b)
#for p in b.board:
#    print(p.to_pos())
#b.move_piece("g2", "g3")
#pp(b)
#pp(b.board)
#b["h1"] = ("white", "p")
#print("pop:", b.pop("a2"))
#pp(b)
#b["h3"] = ("black", "p")
#kpp(b)

test_moves = 'f2f4 d7d5 e2e4 e7e6 c2c4 d5d4 d2d3 b8d7'


nb = ch.step_moves("", test_moves)
nb[-1].print_board()



#r = 7
#c = "h"
#print(ch.BOARD_ROWS[::-1][r])
#print(ch.BOARD_COLS.index(c))
#
#p = ch.Piece("white", "p", pos="h2")
#print(p)
#print(p)
#print("1: ", ch.Piece("white", "p", pos="h2"))
#print("2: ", ch.Piece("white", "n", pos="a2"))
#print("3: ", ch.Piece("white", "k", "a", 3))
#print(p.to_pos())
#
#print("x: ", p.to_x())
#print("y: ", p.to_y())
#print("yx: ", p.to_yx())
#print("xy: ", p.to_xy())
#
###p1 = ch.Piece("white", "r")
###p2 = ch.Piece("white", "k")
###
###def po(c,r):
###    return f"{c}{r}"
###
###fr = ("r","n","b","q","k","b","n","r")
###br = tuple("p" for x in range(1,9))
###b = ch.Board()
###pp(b)
###b["a1"] = p1
###pp(b)
###b["h2"] = p2
###pp(b)
####CHESS_COLS = ('a', #'',
###row_matric = tuple(col for col in ch.row_range())
###print(row_matric)
###
###BOARD_FRONT_ROW = ("p","p","p","p","p","p","p","p")
###BOARD_BACK_ROW = ("r","n","b","q","k","b","n","r")
###BOARD_ROWS = (1, 2, 3, 4, 5, 6, 7, 8)
###BOARD_COLS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
###BOARD_MATRIX = tuple(tuple(po(col,row) for col in BOARD_COLS) for row in BOARD_ROWS)
###pp(BOARD_MATRIX)
###
###print("1: ", [po(col, row) for row in (7,8) for col in BOARD_COLS])
###
###print("2: ", [(pos,piece,ch.Black) for pos, piece in zip([po(col, row) for row in (7,8) for col in BOARD_COLS], fr+br)])
###
####BOARD_START_PIECES = [
###def xr(r):
###    return tuple(po(c,r) for c in BOARD_COLS)
###    
###def xt(side, front, back):
###    for pos, piece  in zip(xr(front) + xr(back), BOARD_FRONT_ROW + BOARD_BACK_ROW):
###        print(pos, piece )
###    #zip(xr(8), BOARD_FRONT_ROW)
###print("4: ", xt(ch.White, 7, 8))
###]
###def start_pieces(side, front_row, back_row):
###    for pos, piece in ):
###        yield pos, ch.Piece(side, piece)
###    for pos, piece in zip((po(c,fron_row) for c in BOARD_COLS),tuple("p" for i in range(1,8+1))):
###        yield pos, ch.Piece(side, piece)
##
###print("!white!")
###for piece in start_pieces(ch.White, 2):
###    print(piece)
###print("white back")
####for piece in start_pieces(ch.White, 1):
####    print(piece)
####
####print("black front")
####for piece in start_pieces(ch.Black, 7):
####    print(piece)
###print("!black!")
###for piece in start_pieces(ch.Black, 8):
###    print(piece)
##
###start_pieces_front(ch.White, 7)
##br = tuple("p" for x in range(1,9))
###print("2: ", [(pos,piece,ch.White) for pos, piece in zip([po(col, row) for row in (2,1) for col in BOARD_COLS], fr+br)])
##
###def start(side, start_rows):
###    print("3: ", [(pos,piece,side) for pos, piece in zip([po(col, row) for row in start_rows for col in BOARD_COLS], fr+br)])
###start(ch.White, (7,8))
##
##
###pp(BOARD_ROWS[-2:])
###pp(BOARD_ROWS[:2])
##print("bello!")
##
##
##sr = fr + br
##
##board = {
##}
##
##white_start = [ch.row_positions(row) for row in (7,8)]
##print(white_start)
##    #poss = [(po(col,row)) for row in (side.front_row_nr,side.back_row_nr) for col in ch.col_range()]
##
##
##print("HI!")
##for i in fr + br:
##    print(i)
##print("mid!")
##
##
##
##def player_start(side):
##    poss = [(po(col,row)) for row in (side.front_row_nr,side.back_row_nr) for col in ch.col_range()]
##    print(poss)
##player_start(ch.White)
###pp([(pos, piece) for pos, piece in zip(poss,fr+br)])
##
###for row in (7,8):
###    for col in ch.col_range():
###        print(po(col,row))
##print("bye!")
##    
###for j in zip(ch.row_positions(7), ch.row_positions(7)):
##    #print(row)
##    
##wfr = [
##    [ch.Piece(side, piece) for piece in fr ]
##    for side in (ch.White, ch.Black)
##]
##pp(wfr)
##
##
##
##print("white pieces!")
##s = ch.White
##r = 7
##c = "h"
##
###print([(c,r) for col in ch.col_range()])
###stuff =[(side, front, back) for side, front, back in ((ch.White, 1, 2, fr,), (ch.Black, 8, 7))]
##pp(stuff)
###pp([[pos,variant] for pos in ch.row_positions(r) for variant in fr])
##
###for pos, piece in zip(ch.row_positions(r), fr):
##    #print(pos, piece)
##
##    
###for p in fr:
###    fp1 = ch.Piece(ch.White,p)
##
##
##
##print("black pieces!")
##
###sides = (ch.White, ch.Black)
##
###WHITE_PLAYER_START = [ch.Piece(side, variant]
##
##
##print("start pieces")
###for side in (ch.White, ch.Black):
###    print(side)
###    for piece, pos
###start_pieces_side(7, fr)
###def sp(side, variant):
##
###    pass
##for side in sides:
#    #for variant in 
##wp = [ch.Piece(side, variant) for variant in fr for side in sides]
##print("here!")
##pp(wp)
#
##for it in zip(ch.row_positions(8),br):
#    #print(it)
#    
#
##for side, front_row, back_row in ((ch.White, ch.Black), fr, br):
#
##    pi = Piece(side)
#
#
#
##pp(fr)
##pp(br)
#
##a = [(pos, side) front, back# for side in [ch.White, ch.Black] for pos in ch.row_positions(side.back_row_nr) ]
##pp(a)
##for x in a:
##    print(x)
#
#
##c = ch.col_positions("c")
##r = ch.row_positions("1")
##pp(c)
##pp(r)
##eb = ch.empty_board()
##pp(eb)
##nb = ch.new_board()
##bv = ch.Board()
##print(bv["a2"])
##pp(bv.position)
##pos = ch.Position("a","4",ch.Piece("white","b"))
##pce = ch.Piece("white","b")
##bv["a4"] = pce
##
##
##br = bv.pop("a2")
##
##pp(br)
##pp(bv.position)
