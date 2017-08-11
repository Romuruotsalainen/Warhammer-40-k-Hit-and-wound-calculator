from spaceMarine import spacemarine
from weapon import weapon
from to_wound import to_wound
import random
import numpy

tactical_marine = spacemarine(3, 3, 4, 4, 4, 3, 8, 3)
bolter = weapon("Bolter", 24, "Rapid Fire 1", 4, 0, 1, "")

def to_hit_ranged(bs):
    bs_dice = [6, 5, 4, 3, 2, 1] #Dice required to hit
    toHit = bs_dice[bs - 1]
    diceRoll = random.randrange(1, 7)
    if diceRoll >= toHit:
        return True
    else:
        return False


def toWound(toughness, strength):
    diceRoll = random.randint(1, 7)
    strengt_toughness_chart = to_wound(toughness, strength)
    if diceRoll >= strengt_toughness_chart.wound():
        return True
    else:
        return False

def main():
    if to_hit_ranged(3):
        print("You hit!")
        if  toWound(4, 4):
            print("You wounded it")
        else:
            print("It survived.")
    else:
        print("You missed.")

main()
