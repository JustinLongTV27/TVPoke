from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        self.activeTrainer = self.trainers[0]
        
    def elementsToDisplay(self):
        self.elements = []

        for trainer in self.trainers:
            if trainer == self.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2

        for trainer in self.trainers:
            self.elements.extend(trainer.getPageElements())

        for trainer in self.trainers:
            if self.activeTrainer == trainer:
                trainer.postion = 1
            else:
                trainer.position = 2

        if self.activeTrainer == self.trainers[0]:
            self.activeTrianer = self.trainers[1]
        else:
            self.activeTrainer = self.trainers[0]



class BattleButtons(Button):
    def __init__(self, position, width, height, text, imgPath):
        super().__init__(position, width, height, text)
        self.imgPath = imgPath


class BackRound(Image):
    def __init__(self, position, width, height, img):
        super().__init__(position, width, height, img)

        #y = 0
        ##two rows of three
        #for trainer in self.trainers:
        #    x = 0
        #    y += 100/3
        #    for poke in trainer.pokemon:
        #        x += 100/4
        #        self.elements.append(Image((x, y), 20, 20, poke.img))
        #        self.elements.append(Label((x, y + 10), 20, 10, poke.name))