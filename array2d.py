from pyarray import Array
import itertools

class Array2D:
    def __init__(self,rows,cols):
        self.theRows=Array(rows)
        for i in range(rows):
            self.theRows[i]=Array(cols)

    def numrows(self):
        return (len(self.theRows))

    def numcols(self):
        return (len(self.theRows[0]))

    def clear(self,value):
        for i in range(self.numrows()):
            self.theRows[i].clear(value)

    def __getitem__(self,pos):
        assert len(pos)==2,"Two subscripts required."
        i=pos[0]
        j=pos[1]
        assert i>=0 and i<self.numrows()\
               and j>=0 and j<self.numcols(),\
        "Invalid element subscript"
        return self.theRows[i][j]

    def __setitem__(self,pos,value):
        assert len(pos)==2,"Two subscripts required."
        i=pos[0]
        j=pos[1]
        assert i>=0 and i<self.numrows()\
               and j>=0 and j<self.numcols(),\
        "Invalid element subscript"
        self.theRows[i][j]=value

    def traverse(self):
        x=self.numrows()
        y=self.numcols()
        for i in range(x):
            for j in range(y):
                print(self.theRows[i][j], end=" ")
            print()
    def SelectedTraversal(self,From,To):
        assert type(From)==tuple and type(To)==tuple,"Two subscripts required."
        lst=[]
        #For vertical traversal
        if From[1] == To[1]:
            if From[0]>To[0]:
                direct = -1
            else:
                direct = 1
            for i in range(From[0],To[0],direct):
                lst.append(self.theRows[i][From[1]])
        #For horizontal traversal
        elif From[0] == To[0]:
            if From[1]>To[1]:
                direct = -1
            else:
                direct = 1
            for j in range(From[1],To[1],direct):
                lst.append(self.theRows[From[0]][j])
        #For diagnol traversal
        #elif To[0]-From[0] == To[1]-From[1]:
        else:
            if From[0]>To[0]:
                direct1 = -1
            else:
                direct1 = 1
            if From[1]>To[1]:
                direct2 = -1
            else:
                direct2 = 1
            for i,j in zip(range(From[0],To[0],direct1),range(From[1],To[1],direct2)):
                lst.append(self.theRows[i][j])
        return lst
    #def SelectedTraversal(self,From,To):
    #    if From[0] > To[0]:
    #        direct1 = -1
    #    else:
    #        direct1 = 1
    #    if From[1] > To[1]:
    #        direct2 = -1
    #    else:
    #        direct2 = 1
    #    for i,j in itertools.zip_longest(range(From[0],To[0],direct1),range(From[1],To[1],direct2)):
    #       pass

