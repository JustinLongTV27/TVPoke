from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.state = {
            "goTo" : ""
        }
        self.loser = ""
        self.winner = ""

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        self.activeTrainer = self.trainers[0]
        
        for trainer in self.trainers:
            if trainer == self.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2

        self.trainers[0].name = "Player 1"
        self.trainers[1].name = "Player 2"
    
    def checkLoser(self):
        for trainer in self.trainers:
            if len(trainer.pokemon) == 0:
                self.loser = trainer.name
                for  guy in self.trainers:
                    if guy != trainer:
                        self.winner = guy.name
                        self.state["goTo"] = "WIN"
                break
                
        
    def elementsToDisplay(self):
        self.elements = [
            BackRound(),
        ]

        self.checkLoser()

        for trainer in self.trainers:
            self.elements.extend(trainer.getPageElements())

        if self.loser != "":
            pass
        else:
            for i, move in enumerate(self.activeTrainer.pokemon[0].moves):
                x = 75 + (i % 2) * 15
                y = 10 + (i // 2) * 15
                self.elements.append(BattleButtons((x, y), move))

            


class BattleButtons(Button):
    def __init__(self, centerXY, move):
        super().__init__(centerXY, 15, 20, (255, 255, 255), (0, 0, 0))
        self.move = move
        self.text = self.move.name

    def onClick(self, screen):
        print("you clicked on: " + self.move.name)
        print("You did: " + str(self.move.power) + " Damage!")
        for trainer in screen.trainers:
            if trainer != screen.activeTrainer:
                trainer.pokemon[0].takeDamage(self.move)
                trainer.removeFaintedPokemon()
            else:
                pass
        screen.activeTrainer.removeFaintedPokemon()

        if screen.activeTrainer == screen.trainers[0]:
            screen.activeTrainer = screen.trainers[1]
        else:
            screen.activeTrainer = screen.trainers[0]

        for trainer in screen.trainers:
            if trainer == screen.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2






class BackRound(Image):
    def __init__(self):
        super().__init__((50, 50), 100, 100, "./imgs/pokeBK.png")

    def onClick(self, screen):
        print("")

        #y = 0
        ##two rows of three
        #for trainer in self.trainers:
        #    x = 0
        #    y += 100/3
        #    for poke in trainer.pokemon:
        #        x += 100/4
        #        self.elements.append(Image((x, y), 20, 20, poke.img))
        #        self.elements.append(Label((x, y + 10), 20, 10, poke.name))