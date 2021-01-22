class ColorSelector:
    def __init__(self):
        self.colorList = ["red", "green"]

    def selectColor(self, status):
        if status:
            return self.colorList[1]

        else:
            return self.colorList[0]