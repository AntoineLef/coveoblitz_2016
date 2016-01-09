from random import choice
import time
import math
from game import Game

class Bot:

    def __init__(self):
        self.wantedPosition = 1
        self.lastMove = None

    def calculateThreshold(self, Hero, tileNumber, pikeNumber, gettingMine):
        mineCost = 25
        moveCost = 1
        pikeCost = 10
        cost = tileNumber*moveCost + pikeNumber*pikeCost
        if (gettingMine):
            cost = tileNumber*moveCost + pikeNumber*pikeCost + mineCost
        if (Hero.life == 100 and (cost< Hero.life-20) or (Hero.life >= 35 and (cost< Hero.life-20))):
            return True
        return False

    def move(self, state):
        game = Game(state)

        loc = (game.myHero.pos["x"], game.myHero.pos["y"])
        possibleMove = ["North", "South", "East", "West"]
        passables = []
        for move in possibleMove:
            pos = game.board.to(loc, move)
            if(game.board.is_mine(pos) and game.mines_locs[pos] != str(game.myHero.id)):
                return move
            elif(game.board.is_tavern(loc) and game.myHero.life <= 50):
                return move

            elif(game.board.passable(pos)):
                passables.append(move)
        else:
            return choice(passables)


class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'Eastest', 'East', 'South', 'North']
        return choice(dirs)

