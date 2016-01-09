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
        loc = game.myHero.pos;
        if (deltaX < deltaY):
            if (deltaX < 0):
                x, y = loc
                x -=1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'West'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)
            else:
                x, y = loc
                x +=1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'East'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)
        else:
            if (deltaY < 0):
                x, y = loc
                y -=1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'South'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)
            else:
                x, y = loc
                y +=1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'North'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)

    def move(self, state):
        game = Game(state)
        game.heroes_locs.keys
        game.mines_locs
        game.spikes_locs
        game.taverns_locs
        self.getNearestEnemy(game.myHero, game.mines_locs)

    def getNearestMine(self, myHero, mines_locs):
        mines_locs

    def distance(self, pos1, pos2):
        x = (pos2[0] - pos1[0])
        y = (pos2[1] - pos1[1])
        return (x,y)
    pass

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

