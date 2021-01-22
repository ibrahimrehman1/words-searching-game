class word:
    def __init__(self,data):
        self.spelling = data
        self.letters = list(data)
    def setAttributes(self,ori,pos):
        self.orientation=ori
        self.position=pos
        self.coordinates=[]