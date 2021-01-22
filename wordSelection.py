from random import randrange

class WordsSelector:
    def __init__(self):
        self.lst = []
        self.loadWords()
        self.selectedWords = []
        self.chooseWords()
    def loadWords(self):
        with open("words.txt", "rt") as f:
            self.lst = f.readlines()[0].lower().split(" ")

    def chooseWords(self):
        i = 0
        while i < 10:
            a = self.lst[randrange(0, len(self.lst))]
            if a not in self.selectedWords:
                self.selectedWords.append(a)
                i += 1

        
        


