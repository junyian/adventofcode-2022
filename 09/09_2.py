class Rope:
    def __init__(self):
        self.h_row, self.t_row, self.h_col, self.t_col = 0, 0, 0, 0
        self.paths = set()
    
    def movehead(self, dir):
        if dir=='L':
            self.h_col -= 1
        elif dir=='R':
            self.h_col += 1
        elif dir=='U':
            self.h_row -= 1
        elif dir=='D':
            self.h_row += 1
    
    def movetail(self):
        if self.t_row==self.h_row and self.t_col==self.h_col-2:     # .T.H.
            self.t_col += 1
        elif self.t_row==self.h_row and self.t_col==self.h_col+2:   # .H.T.
            self.t_col -= 1
        elif self.t_row==self.h_row-2 and self.t_col==self.h_col:   # .T.
            self.t_row += 1                                         # ...
                                                                    # .H.

        elif self.t_row==self.h_row+2 and self.t_col==self.h_col:   # .H.
            self.t_row -= 1                                         # ...
                                                                    # .T.

        elif self.t_row==self.h_row+2 and self.t_col==self.h_col+1: # H.
            self.t_row -= 1                                         # ..
            self.t_col -= 1                                         # .T
        
        elif self.t_row==self.h_row+2 and self.t_col==self.h_col-1: # .H
            self.t_row -= 1                                         # ..
            self.t_col += 1                                         # T.
        
        elif self.t_row==self.h_row+1 and self.t_col==self.h_col-2: # H..
            self.t_row -= 1                                         # ..T
            self.t_col -= 1
            
            