from go import *

s = BoardState()
s.change(9,9,Black)
s.change(9,10,Black)
s.change(8,11,Black)
s.change(7,11,Black)
s.change(6,11,Black)
s.change(5,10,Black)
s.change(8,9,Black)
s.change(5,9,Black)
s.change(5,8,Black)
s.change(6,8,Black)
s.change(7,8,Black)
s.change(8,8,Black)
s.change(6,9,White)
s.change(6,10,White)
s.change(7,9,White)
s.change(7,10,White)
s.change(8,10,White)

s.change(1,1,Black)
s.change(1,2,Black)
s.change(2,1,White)
s.change(2,2,White)
s.change(1,3,White)

s.change(14,13,Black)
s.change(15,14,Black)
s.change(13,14,Black)
s.change(14,14,White)

s.change(14,16,White)
s.change(14,17,Black)
s.change(15,16,Black)
s.change(13,16,Black)

s.change(14,15,Black)

s.display_matrix()
print "(8,9)   captures:", s.capture_list((8,9))
print "(6,11)  captures:", s.capture_list((6,11))
print "(1,3)   captures:", s.capture_list((1,3))
print "(14,15) captures:", s.capture_list((14,15))