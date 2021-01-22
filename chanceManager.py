class ChanceManager:
    def __init__(self):
        self.chances = 10

    def updateChances(self):
        self.chances -= 1
        return self.chances == 0