from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Nukemon(Normal):
    def __init__(self):
        moves = [
            Move("Gods fist", "FIRE", 999),
            Move("Gods divine rule", "FIRE", 999),
            Move("Steel shockwave", "FIRE", 999),
            Move("Divine fire ball", "FIRE", 999)
        ]
        super().__init__("Rules set by God", 999, moves, "./TVPoke/Pokemon/imgs/Nukemon.png")