import importlib
from PyUI.PageElements import Label, Image

class Trainer:
    def __init__(self, pokemon):
        self.pokemon = []
        self.position = 1
        self.name = "Trainer"
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

        if len(self.pokemon) > 0:
            pokeHealth = self.pokemon[0].hp
            pokeName = self.pokemon[0].name
            pokeImg = self.pokemon[0].img

            if len(self.pokemon) > 0:
                if self.position == 1:
                    pokeX = 25
                    pokeY = 25

                    healthLabel = Label((pokeX, pokeY + 20), 20, 10, "Your " + pokeName + " HP: " + str(pokeHealth))
                    elements.append(healthLabel)
                    thePokemon = Image((pokeX, pokeY - 7), 40, 40, pokeImg)
                    elements.append(thePokemon)
                else:
                    pokeX = 75
                    pokeY = 75

                    healthLabel = Label((pokeX, pokeY + 5), 20, 10, pokeName + " Enemy HP: " + str(pokeHealth))
                    thePokemon = Image((pokeX + 3, pokeY - 11), 20, 20, pokeImg)

                elements.append(healthLabel)
                elements.append(thePokemon)
                return elements
            else:
                return elements
        else:
            return elements