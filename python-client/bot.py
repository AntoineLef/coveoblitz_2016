from random import choice
import time
import math
from game import Game

class Bot:

    def __init__(self):
        self.wantedPosition = 1

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

    def move(self, state):
        game = Game(state)
        loc = game.myHero.pos;
        deltaX, deltaY = self.getNearestMine(game.myHero, game.mines_locs)
        loc = (game.myHero.pos["x"], game.myHero.pos["y"])
        if (abs(deltaX) < abs(deltaY)):
            if (deltaX < 0):
                x, y = loc
                x -= 1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'West'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)
            else:
                x, y = loc
                x += 1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'East'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)
        else:
            if (deltaY < 0):
                x, y = loc
                y -= 1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'South'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)
            else:
                x, y = loc
                y += 1
                loc = (x, y)
                if (game.board.passable(loc)):
                    return 'North'
                else:
                    dirs = ['Stay', 'North', 'South', 'East', 'West']
                    return choice(dirs)


    def getNearestMine(self, myHero, mines_locs):
        not_owned_mine = [];
        for mine in mines_locs.keys():
            if(mines_locs[mine] != myHero.id):
                not_owned_mine.append(mine)

        deltaX = 999999
        deltaY = 999999

        for mine_position in not_owned_mine:
            distance_calculated = self.distance(myHero.pos, mine_position)
            if(deltaX + deltaY > distance_calculated[0] + distance_calculated[1]):
                deltaX = distance_calculated[0]
                deltaY = distance_calculated[1]
                self.wantedPosition = distance_calculated

        return (deltaX, deltaY)
    pass

    def getNearestBeer(self, myHero, beer_location):
        deltaX = 999999
        deltaY = 999999

        for beer_position in beer_location.key():
            distance_calculate = self.distance(myHero.pos, beer_position)
            if(deltaY + deltaX > distance_calculate[0] + distance_calculate[1]):
                deltaX = distance_calculate[0]
                deltaY = distance_calculate[1]
        return(deltaX, deltaY)
    def distance(self, pos1, pos2):
        x = (pos2[0] - pos1["y"])
        y = (pos2[1] - pos1["x"])
        return (x,y)
    pass

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

