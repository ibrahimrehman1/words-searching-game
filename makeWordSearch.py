from array2d import Array2D
from Word import word
import random
import tkinter as tk

class makeWordSearch:
    def __init__(self,lst):
        self.word2DArray = Array2D(10,10)
        self.orientations = ["VerticalDown", "VerticalUp", "HorizontalRight", "HorizontalLeft",
                             "FirstDiagnol", "SecondDiagnol", "RevFirstDiagnol", "RevSecondDiagnol"]
        self.wordList = []
        for i in lst:
            a = word(i)
            self.wordList.append(a)
        for wrd in self.wordList:
            while True:
                i = random.randrange(0,self.word2DArray.numrows())
                j = random.randrange(0,self.word2DArray.numcols())
                pos = (i,j)
                check = self.chooseOrientation(pos,wrd)
                if check[0]:
                    orient = random.choice(check[1])
                    wrd.setAttributes(orient,pos)
                    self.arrangeWord(wrd)
                    break
        self.fillGaps()
        self.initialPos = [i.position for i in self.wordList]

    def arrangeWord(self,wrd):
        i=wrd.position[0]
        j=wrd.position[1]
        for let in wrd.letters:
            self.word2DArray[i, j] = let
            wrd.coordinates.append((i,j))
            if wrd.orientation == "VerticalDown":
                i+=1
            elif wrd.orientation == "VerticalUp":
                i-=1
            elif wrd.orientation == "HorizontalRight":
                j+=1
            elif wrd.orientation == "HorizontalLeft":
                j-=1
            elif wrd.orientation == "FirstDiagnol":
                i+=1
                j+=1
            elif wrd.orientation == "SecondDiagnol":
                i+=1
                j-=1
            elif wrd.orientation == "RevFirstDiagnol":
                i-=1
                j-=1
            elif wrd.orientation == "RevSecondDiagnol":
                i-=1
                j+=1

    def compareLists(self,stan,comp):
        for i, n in enumerate(stan):
            if n is not None and n != comp[i]:
                return False
        return True

    def chooseOrientation(self,pos,wrd):
        assert type(wrd)==word
        assert type(pos)==tuple
        if self.word2DArray[pos] is not None and self.word2DArray[pos] != wrd.letters[0]:
            return [False, []]
        availableOrientations = [i for i in self.orientations]
        i = pos[0]
        j = pos[1]
        l = len(wrd.letters)
        if i+len(wrd.letters)-1 > self.word2DArray.numrows()-1:
            availableOrientations.remove("VerticalDown")
            availableOrientations.remove("FirstDiagnol")
            availableOrientations.remove("SecondDiagnol")
        if i-len(wrd.letters)+1 < 0:
            availableOrientations.remove("VerticalUp")
            availableOrientations.remove("RevFirstDiagnol")
            availableOrientations.remove("RevSecondDiagnol")
        if j+len(wrd.letters)-1 > self.word2DArray.numcols()-1:
            availableOrientations.remove("HorizontalRight")
            try:
                availableOrientations.remove("FirstDiagnol")
            except ValueError:
                pass
            try:
                availableOrientations.remove("RevSecondDiagnol")
            except ValueError:
                pass
        if j-len(wrd.letters)+1 < 0:
            availableOrientations.remove("HorizontalLeft")
            try:
                availableOrientations.remove("SecondDiagnol")
            except ValueError:
                pass
            try:
                availableOrientations.remove("RevFirstDiagnol")
            except ValueError:
                pass
        iterList = [i for i in availableOrientations]
        for ori in iterList:
            if ori == "VerticalDown":
                To = (i+l,j)
            elif ori == "VerticalUp":
                To = (i-l, j)
            elif ori == "HorizontalRight":
                To = (i,j+l)
            elif ori == "HorizontalLeft":
                To = (i,j-l)
            elif ori == "FirstDiagnol":
                To = (i+l,j+l)
            elif ori == "SecondDiagnol":
                To = (i+l,j-l)
            elif ori == "RevFirstDiagnol":
                To = (i-l,j-l)
            elif ori == "RevSecondDiagnol":
                To = (i-l,j+l)
            a = self.word2DArray.SelectedTraversal(pos, To)
            if a.count(a[0]) != len(a):
                if not self.compareLists(a,wrd.letters):
                    availableOrientations.remove(ori)
        return [len(availableOrientations)>0, availableOrientations]


    def fillGaps(self):
        x=self.word2DArray.numrows()
        y=self.word2DArray.numcols()
        for i in range(x):
            for j in range(y):
                if self.word2DArray[i,j] == None:
                    self.word2DArray[i,j] = chr(random.randrange(97, 97 + 26))

    def getWord2DArray(self):
        return self.word2DArray
