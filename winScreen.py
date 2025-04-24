from PyUI.Screen import Screen
from PyUI.PageElements import *

class WinScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (255,250,253))
        self.winner = ""
        self.state = {
            "goto" : ""
        }

    def elementsToDisplay(self):
        self.elements = [
            Label((50, 50), 20, 10, self.winner + " has won!", 40),
        ]