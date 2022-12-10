import numpy
import sys

lines = open("input2.txt").readlines()

class Rope:
    def __init__(self, size=6, startrow=0, startcol=0):
        self.size = size
        self.h_row, self.t_row, self.h_col, self.t_col = startrow, startrow, startcol, startcol
        self.paths = set()
        self.mapmask = numpy.zeros((self.size, self.size), int)
    
    def movehead(self, direction):
        if direction=='L':
            self.h_col -= 1
        elif direction=='R':
            self.h_col += 1
        elif direction=='U':
            self.h_row += 1
        elif direction=='D':
            self.h_row -= 1
    
    def movetail(self):
        if self.t_row==self.h_row and self.t_col==self.h_col-2:     # .T.H.
            self.t_col += 1
        elif self.t_row==self.h_row and self.t_col==self.h_col+2:   # .H.T.
            self.t_col -= 1
        elif self.t_row==self.h_row+2 and self.t_col==self.h_col:   # .T.
            self.t_row -= 1                                         # ...
                                                                    # .H.

        elif self.t_row==self.h_row-2 and self.t_col==self.h_col:   # .H.
            self.t_row += 1                                         # ...
                                                                    # .T.

        elif self.t_row==self.h_row-2 and self.t_col==self.h_col+1: # H.
            self.t_row += 1                                         # ..
            self.t_col -= 1                                         # .T
        
        elif self.t_row==self.h_row-1 and self.t_col==self.h_col+2: # H..
            self.t_row += 1                                         # ..T
            self.t_col -= 1

        elif self.t_row==self.h_row-2 and self.t_col==self.h_col-1: # .H
            self.t_row += 1                                         # ..
            self.t_col += 1                                         # T.
        
        elif self.t_row==self.h_row-1 and self.t_col==self.h_col-2: # ..H
            self.t_row += 1                                         # T..
            self.t_col += 1
        
        elif self.t_row==self.h_row+2 and self.t_col==self.h_col+1: # .T
            self.t_row -= 1                                         # ..
            self.t_col -= 1                                         # H.
        
        elif self.t_row==self.h_row+1 and self.t_col==self.h_col+2: # ..T
            self.t_row -= 1                                         # H..
            self.t_col -= 1
        
        elif self.t_row==self.h_row+2 and self.t_col==self.h_col-1: # T.
            self.t_row -= 1                                         # ..
            self.t_col += 1                                         # .H
        
        elif self.t_row==self.h_row+1 and self.t_col==self.h_col-2: # T..
            self.t_row -= 1                                         # ..H
            self.t_col += 1
        
        elif self.t_row==self.h_row-2 and self.t_col==self.h_col-2: # ..H
            self.t_row += 1                                         # ...
            self.t_col += 1                                         # T..
        
        elif self.t_row==self.h_row+2 and self.t_col==self.h_col+2: # ..T
            self.t_row -= 1                                         # ...
            self.t_col -= 1                                         # H..

        elif self.t_row==self.h_row-2 and self.t_col==self.h_col+2: # H..
            self.t_row += 1                                         # ...
            self.t_col -= 1                                         # ..T

        elif self.t_row==self.h_row+2 and self.t_col==self.h_col-2: # T..
            self.t_row -= 1                                         # ...
            self.t_col += 1                                         # ..H

        # else:
        #     print("unhandled position")
        
        self.paths.add((self.t_row, self.t_col))
        # print(self.paths)

    def printcoords(self):
        print(f"H: row={self.h_row} col={self.h_col}")
        print(f"T: row={self.t_row} col={self.t_col}")
    
    def printmap(self):
        self.map = numpy.array(['.']*self.size*self.size).reshape(self.size,self.size)
        if self.h_row==self.t_row and self.h_col==self.t_col:
            self.map[self.h_row][self.h_col] = 'H'
        else:
            self.map[self.h_row][self.h_col] = 'H'
            self.map[self.t_row][self.t_col] = 'T'
        for i in range(self.size-1, -1, -1):
            for j in range(self.size):
                print(self.map[i][j],end='')
            print()
        print()

# Part 1
# rope = Rope(20, 11, 11)
rope = Rope(20, 0, 5)

# rope.printcoords()
# rope.printmap()
# print(rope.mapmask)

for i, l in enumerate(lines):
    # print(f"Line {i}:")
    dir, count = l.strip().split(' ')
    for i in range(int(count)):
        # print(dir)
        
        rope.movehead(dir)
        rope.movetail()
        
        # rope.printcoords()
        # print(rope.paths)
        # rope.printmap()

# # print(rope.paths)
print(len(rope.paths))

# Part 2
# ropes = [Rope(20, 0, 0), Rope(20, 0, 0), Rope(20, 0, 0), Rope(20, 0, 0), Rope(20, 0, 0), Rope(20, 0, 0), Rope(20, 0, 0), Rope(20, 0, 0), Rope(20, 0, 0)]
ropes = [
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
    Rope(30, 10, 15),
]

def printmap(ropes):
    map = numpy.array(['.']*30*30).reshape(30,30)
    for i,r in enumerate(ropes):
        if i==0:
            map[r.h_row][r.h_col] = 'H'
        else:
            if map[r.h_row][r.h_col] == '.':
                map[r.h_row][r.h_col] = str(i)
    for i in range(map.shape[0]-1, -1, -1):
        for j in range(map.shape[0]): 
            print(map[i][j],end='')
        print()
    print()

for i, l in enumerate(lines):
    # print(f"Line {i}:")
    dir, count = l.strip().split(' ')
    # print(dir, int(count))
    for i in range(int(count)):
        # print(f"Count {i+1}")
        for j in range(len(ropes)):
            if j==0:
                ropes[j].movehead(dir)
                ropes[j].movetail()
            else:
                ropes[j].h_row = ropes[j-1].t_row
                ropes[j].h_col = ropes[j-1].t_col
                ropes[j].movetail()
                # if j==len(ropes)-1:
                    # print("dbg: ", ropes[j].t_row, ropes[j].t_col)
            # print()
        # printmap(ropes) 
        # print(ropes[-2].paths)
        # input()

# print(ropes[-2].paths)
print(len(ropes[-2].paths))