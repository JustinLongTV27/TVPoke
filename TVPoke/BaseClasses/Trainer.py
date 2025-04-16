import importlib
from PyUI.PageElements import Label, Image

class Trainer:
    def __init__(self, pokemon):
        self.pokemon = []
        for poke in pokemon:
            pokeFile = importlib.import_module("TVPoke.Pokemon." + poke)
            PokeClass = getattr(pokeFile, poke)
            self.pokemon.append(PokeClass())

    def removeFaintedPokemon(self):
        for poke in self.pokemon:
            if poke.hp <= 0:
                self.pokemon.remove(poke)

    def getPageElements(self):
        elements = []

        pokeHealth = self.pokemon.hp
        pokeName = self.pokemon.name
        pokeImg = self.pokemon.imgPath

        if self.position == 1:
            pokeX = 25
            pokeY = 25
            
            healthLabel = Label((pokeX, pokeY), 20, 10, pokeName + "Your HP: " + pokeHealth)
            thePokemon = Image((pokeX, pokeY), 20, 20, pokeImg)
            elements.append(healthLabel)
            elements.append(thePokemon)
        else:
            pokeX = 75
            pokeY = 75

            healthLabel = Label((pokeX, pokeY), 20, 10, pokeName + "Enemy HP: " + pokeHealth)
            thePokemon = Image((pokeX, pokeY), 20, 20, pokeImg)
            elements.append(healthLabel)
            elements.append(thePokemon)