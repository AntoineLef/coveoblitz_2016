from random import choice
import time
from game import Game

class Bot:

    def calculateThreshold(self, Hero, tileNumber, pikeNumber, gettingMine):
        mineCost = 25
        moveCost = 1
        pikeCost = 10
        cost = tileNumber*moveCost + pikeNumber*pikeCost
        if (gettingMine ):
            cost = tileNumber*moveCost + pikeNumber*pikeCost + mineCost
        if (Hero.life == 100 & (cost< Hero.life-20)| (Hero.life >= 35 & (cost< Hero.life-20))):
            return True
        return False

    def move(self, state, deltaX, deltaY):
        game = Game(state)
        loc = game.hero.pos;
        if (deltaX < deltaY):
            if (deltaX < 0):
                x, y = loc
                x -=1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'West'
                return
            else
                return
        else
              if (deltaY < 0):
                return
            else
                return
            return
    pass

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

