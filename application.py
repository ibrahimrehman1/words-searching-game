from wordSelection import WordsSelector
from chanceManager import ChanceManager
from tkinter import Tk, messagebox, Button, Label, Entry, Frame
from colorSelector import ColorSelector
from makeWordSearch import makeWordSearch
from array2d import Array2D



class Application(WordsSelector, ChanceManager, ColorSelector, makeWordSearch):
    def __init__(self):
        self.btnList = [[], [], [], [], [], [], [], [], [], []]
        self.status = False
        self.currentWordCoords = []
        self.currentPos = 0
        self.count = 0
        self.j = None
        self.k = None
        self.track = False
        self.color = None
        ChanceManager.__init__(self)
        WordsSelector.__init__(self)
        ColorSelector.__init__(self)
        makeWordSearch.__init__(self, self.selectedWords)
        self.b = self.getWord2DArray()
        self.build()


    # For Building Game
    def build(self):
        self.root = Tk()
        self.root.title("Word Search")
        self.root.minsize(width=400, height=500)
        self.labelH = Label(self.root, text="Word Search", font='Arial 15 bold')
        self.labelH.grid(row=0)
        self.label1 = Label(self.root, text=f"Remaining Chances: {self.chances}", font="Arial 10 bold", fg='red')
        self.label1.grid(row=1,pady=(0,10))
        f = self.displayWordSearch()
        f.grid(row=2, column=0)
        self.frame1 = Frame(self.root)
        for i,n in enumerate(self.selectedWords):
            lab = Label(self.frame1, text=n, font='Arial 10 bold')
            lab.grid(row=i//5,column=i%5,padx=8)
        self.frame1.grid(row=3, column=0,pady=10)
        self.exitButton = Button(self.root, text="Exit", command=self.destroyGame, fg="white",bg="red", font="Arial 10 bold")
        self.exitButton.grid(row=5,ipadx=5,pady=(0,5))
        self.root.mainloop()


    

    # For Ending Game
    def destroyGame(self):
        self.root.destroy()



    # For Data Submission 
    def submitData(self, coords):
        self.checkData(coords)
        self.color = self.selectColor(self.status)
        if len(self.wordList) == 0:
            messagebox.showinfo('Game won', 'Congratulations! You won the Game!')
            self.destroyGame()
            return
        if self.status:
            self.btnList[coords[0]-1][coords[1]].configure(bg=self.color)

        else:
            self.btnList[coords[0]-1][coords[1]].configure(bg=self.color)
            self.track = self.updateChances()
            self.label1.config(text=f"Remaining Chances: {self.chances}")
            if self.track == True:
                messagebox.showinfo(message="Game Over. You have lost all chances")
                self.destroyGame()
                self.i = None
                self.j = None
                self.count = 0
                self.btnList = [[], [], [], [], [], [], [], [], [], []]
                return


        self.count += 1
        self.j = coords[0]
        self.k = coords[1]


    # For Data Checking
    def checkData(self, coords):
        if coords in self.currentWordCoords and coords == self.currentWordCoords[self.currentPos]:
            self.status = True
            self.currentPos += 1
            if self.currentPos == len(self.currentWordCoords):
                self.currentPos = 0
                self.currentWordCoords=[]
                self.count=0
                self.wordList.remove(self.currentWord)
                self.initialPos.remove(self.currentWord.position)
                self.selectedWords.remove(self.currentWord.spelling)
                for i in self.frame1.winfo_children():
                    i.destroy()
                for i, n in enumerate(self.selectedWords):
                    lab = Label(self.frame1, text=n)
                    lab.grid(row=i // 5, column=i % 5)
                self.frame1.config()
                messagebox.showinfo('Word found','Congratulations! You found a word! '+str(len(self.wordList))+' more to go!')
        elif coords in self.initialPos:
            while self.currentPos>0:
                self.currentPos-=1
                a = self.currentWordCoords[self.currentPos][0]
                b = self.currentWordCoords[self.currentPos][1]
                self.btnList[a-1][b].configure(bg="SystemButtonFace")
            if self.count != 0 and not self.status:
                self.btnList[self.j-1][self.k].configure(bg="SystemButtonFace")
            self.status = True
            self.currentPos += 1
            for wrd in self.wordList:
                if coords == wrd.position:
                    self.currentWord = wrd
                    self.currentWordCoords = wrd.coordinates
        else:
            while self.currentPos>0:
                self.currentPos-=1
                a = self.currentWordCoords[self.currentPos][0]
                b = self.currentWordCoords[self.currentPos][1]
                self.btnList[a-1][b].configure(bg="SystemButtonFace")
            if self.count != 0 and not self.status:
                self.btnList[self.j-1][self.k].configure(bg="SystemButtonFace")
            self.status = False
            self.currentWordCoords = []



    def displayWordSearch(self):
        self.WordSearchFrame = Frame(self.root)
        x=self.word2DArray.numrows()
        y=self.word2DArray.numcols()
        self.Buttons = Array2D(x,y)
        for i in range(x):
            for j in range(y):
                text = self.word2DArray[i,j]
                but = Button(self.WordSearchFrame, text=text, height=2, width=5, command=lambda coords = (i, j): self.submitData(coords))
                self.btnList[i-1].append(but)
                but.grid(row=i,column=j)
        return self.WordSearchFrame




Application()
