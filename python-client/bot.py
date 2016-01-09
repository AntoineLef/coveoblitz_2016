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
        if (Hero.life == 100 and (cost< Hero.life-20) or (Hero.life >= 35 and (cost< Hero.life-20))):
            return True
        return False

    def move(self, state):
        game = Game(state)
        deltaX, deltaY = self.getNearestMine(game.myHero, game.mines_locs)
        loc = (game.myHero.pos["x"], game.myHero.pos["y"])
        print( "In move: ",deltaX, deltaY)
        if (deltaX != 0 and abs(deltaX) < abs(deltaY)):
            if (deltaX < 0):
                x, y = loc
                x -= 1
                lookUpLoc = (x, y)
                mineLook = (y,x)
                if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                    print("West passed")
                    return 'West'
                else:
                    if (deltaY < 0 ):
                        x, y = loc
                        y -= 1
                        lookUpLoc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                            print ("West didn't pass south")
                            return 'South'
                        else:
                            print ("West didn't pass north")
                            return 'North'
                    else:
                        x, y = loc
                        y += 1
                        lookUpLoc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                            print ("West didn't pass North because deltaY")
                            return 'North'
                        else:
                            print ("West didn't pass South because deltaY")
                            return 'South'
            else:
                x, y = loc
                x += 1
                lookUpLoc = (x, y)
                mineLook = (y,x)
                if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                    print ("East passed")
                    return 'East'
                else:
                    if (deltaY < 0 ):
                        x, y = loc
                        y -= 1
                        lookUpLoc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                            print("East didn't passed South")
                            return 'South'
                        else:
                            print("East didn't passed North")
                            return 'North'
                    else:
                        x, y = loc
                        y += 1
                        loc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(loc) or game.mines_locs.has_key(mineLook)):
                            print("East didn't passed North because ")
                            return 'North'
                        else:
                            print("East didn't passed South because")
                            return 'South'
        elif (deltaY != 0):
            if (deltaY < 0):
                x, y = loc
                y -= 1
                lookUpLoc = (x, y)
                mineLook = (y,x)
                if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                    return 'South'
                else:
                    if (deltaY < 0 ):
                        x, y = loc
                        y -= 1
                        lookUpLoc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                            return 'South'
                        else:
                            return 'North'
                    else:
                        x, y = loc
                        y += 1
                        lookUpLoc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                            return 'North'
                        else:
                            return 'South'
            else:
                x, y = loc
                y += 1
                lookUpLoc = (x, y)
                mineLook = (y,x)
                if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                    return 'North'
                else:
                    if (deltaX < 0 ):
                        x, y = lookUpLoc
                        x -= 1
                        lookUpLoc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                            return 'West'
                        else:
                            return 'East'
                    else:
                        x, y = loc
                        x += 1
                        lookUpLoc = (x, y)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or game.mines_locs.has_key(mineLook)):
                            return 'East'
                        else:
                            return 'West'
        else:
            return 'Stay'
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

    def distance(self, pos1, pos2):
        x = (pos2[0] - pos1["y"])
        y = (pos2[1] - pos1["x"])
        return (y,x)
    pass

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

