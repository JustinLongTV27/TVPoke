from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Nukemon(Normal):
    def __init__(self):
        moves = [
            Move("Gods fist", "FIRE", 99999),
            Move("Gods divine rule", "FIRE", 9999),
            Move("Steel shockwave", "FIRE", 999),
            Move("Divine fire ball", "FIRE", 99999999)
        ]
        super().__init__("Rules set by God", 9999, moves, "./TVPoke/Pokemon/imgs/Nukemon.png")