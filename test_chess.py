import src.chess as ch
from pprint import pprint as pp
c = ch.col_positions("c")
r = ch.row_positions("1")
pp(c)
pp(r)
eb = ch.empty_board()
pp(eb)
nb = ch.new_board()
pp(nb)
pos = ch.Position("a","2",ch.Piece("white","b"))
print(pos)
if pos == "a2":
    print("bla")
#pp(ch.new_board())
#bv = ch.Board()
#pp(bv.__dict__)
#print(bv["a2"])
