import numpy
import sys

class Knot:
    def __init__(self, width, height, start_row, start_col):
        self.h_col, self.t_col = start_col, start_col
        self.h_row, self.t_row = start_row, start_row
        self.paths = set()
    
    def printcoords(self):
        print(f"H: row={self.h_row} col={self.h_col}")
        print(f"T: row={self.t_row} col={self.t_col}")

    def move(self, dir):
        if self.h_row == self.t_row and self.h_col == self.t_col: # H
            if dir=='R':
                self.h_col += 1
            elif dir=='L':
                self.h_col -= 1
            elif dir=='U':
                self.h_row -= 1
            elif dir=='D':
                self.h_row += 1
        elif self.h_row==self.t_row and self.h_col==self.t_col+1: #TH
            if dir=='R':
                self.h_col += 1
                self.t_col += 1
            elif dir=='L':
                self.h_col -= 1
            elif dir=='U':
                self.h_row -= 1
            elif dir=='D':
                self.h_row += 1
        elif self.h_row==self.t_row-1 and self.h_col==self.t_col+1: #  H
            if dir=='R':                                            # T
                self.h_col += 1
                self.t_col += 1
                self.t_row -= 1
            elif dir=='L':
                self.h_col -= 1
            elif dir=='U':
                self.h_row -= 1
                self.t_row -= 1
                self.t_col += 1
            elif dir=='D':
                self.h_row += 1
        elif self.h_row==self.t_row-1 and self.h_col==self.t_col: # H
            if dir=='R':                                          # T
                self.h_col += 1
            elif dir=='L':
                self.h_col -= 1
            elif dir=='U':
                self.h_row -= 1
                self.t_row -= 1
            elif dir=='D':
                self.h_row += 1
        elif self.h_row==self.t_row-1 and self.h_col==self.t_col-1: # H
            if dir=='R':                                            #  T
                self.h_col += 1
            elif dir=='L':
                self.h_col -= 1
                self.t_col -= 1
                self.t_row -= 1
            elif dir=='U':
                self.h_row -= 1
                self.t_row -= 1
                self.t_col -= 1
            elif dir=='D':
                self.h_row += 1
        elif self.h_row==self.t_row and self.h_col==self.t_col-1: # HT
            if dir=='R':
                self.h_col += 1
            elif dir=='L':
                self.h_col -= 1
                self.t_col -= 1
            elif dir=='U':
                self.h_row -= 1
            elif dir=='D':
                self.h_row += 1
        elif self.h_row==self.t_row+1 and self.h_col==self.t_col-1: #  T
            if dir=='R':                                            # H
                self.h_col += 1
            elif dir=='L':
                self.h_col -= 1
                self.t_col -= 1
                self.t_row += 1        
            elif dir=='U':
                self.h_row -= 1
            elif dir=='D':
                self.h_row += 1
                self.t_row += 1
                self.t_col -= 1
        elif self.h_row==self.t_row+1 and self.h_col==self.t_col: # T
            if dir=='R':                                          # H
                self.h_col += 1
            elif dir=='L':
                self.h_col -= 1
            elif dir=='U':
                self.h_row -= 1
            elif dir=='D':
                self.h_row += 1
                self.t_row += 1
        elif self.h_row==self.t_row+1 and self.h_col==self.t_col+1: # T
            if dir=='R':                                            #  H
                self.h_col += 1
                self.t_col += 1
                self.t_row += 1
            elif dir=='L':
                self.h_col -= 1
            elif dir=='U':
                self.h_row -= 1
            elif dir=='D':
                self.h_row += 1
                self.t_row += 1
                self.t_col += 1
        else:
            print("unhandled H and T relation")
        self.paths.add((self.t_row, self.t_col))
            

knot = Knot(width=5, height=5, start_row=0, start_col=0)
# sys.exit(0)

lines = open("input1.txt").readlines()

# map.printcoords()

for l in lines:
    dir, count = l.strip().split(' ')
    for i in range(int(count)):
        knot.move(dir)
        # print(dir)
        # map.printcoords()
        # print(map.paths)
# print(map.paths)
print(len(knot.paths))

# Part 2
knot1 = Knot(width=5, height=5, start_row=0, start_col=0)
knot2 = Knot(width=5, height=5, start_row=0, start_col=0)
knot3 = Knot(width=5, height=5, start_row=0, start_col=0)
knot4 = Knot(width=5, height=5, start_row=0, start_col=0)
knot5 = Knot(width=5, height=5, start_row=0, start_col=0)
knot6 = Knot(width=5, height=5, start_row=0, start_col=0)
knot7 = Knot(width=5, height=5, start_row=0, start_col=0)
knot8 = Knot(width=5, height=5, start_row=0, start_col=0)
knot9 = Knot(width=5, height=5, start_row=0, start_col=0)

for l in lines:
    dir, count = l.strip().split(' ')
    for i in range(int(count)):
        knot1.move(dir)
        # print(dir)
        # map.printcoords()
        # print(map.paths)
print(knot1.paths)
print(len(knot1.paths))