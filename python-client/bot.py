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
        if (gettingMine):
            cost = tileNumber*moveCost + pikeNumber*pikeCost + mineCost
        if (Hero.life == 100 and (cost< Hero.life-20) or (Hero.life >= 35 and (cost< Hero.life-20))):
            return True
        return False

    def move(self, state):
        game = Game(state)
        deltaY, deltaX = self.getNearestMine(game.myHero, game.mines_locs)
        loc = (game.myHero.pos["x"], game.myHero.pos["y"])
        print loc
        print( "In move: ",deltaY ,deltaX)
        if (deltaX != 0 and abs(deltaX) > abs(deltaY)):
            if (deltaX < 0):
                x, y = loc
                x -= 1
                lookUpLoc = (y, x)
                mineLook = (y, x)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                    print("West passed")
                    return 'West'
                else:
                    if (deltaY < 0 ):
                        x, y = loc
                        y -= 1
                        lookUpLoc = (y, x)
                        mineLook = (y, x)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            print ("West didn't pass Y")
                            return 'South'
                        else:
                            print ("West didn't pass X")
                            return 'North'
                    else:
                        x, y = loc
                        y += 1
                        lookUpLoc = (y, x)
                        mineLook = (y, x)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            print ("West didn't pass X because deltaY")
                            return 'North'
                        else:
                            print ("West didn't pass Y because deltaY")
                            return 'South'
            else:
                x, y = loc
                x += 1
                lookUpLoc = (y, x)
                mineLook = (y, x)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                    print lookUpLoc
                    print ("Z passed")
                    return 'East'
                else:
                    if (deltaY < 0 ):
                        x, y = loc
                        y -= 1
                        lookUpLoc = (y, x)
                        mineLook = (y, x)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            print("Z didn't passed Y")
                            return 'South'
                        else:
                            print("Z didn't passed X")
                            return 'North'
                    else:
                        x, y = loc
                        y += 1
                        loc = (y, x)
                        mineLook = (y,x)
                        if (game.board.passable(loc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            print("Z didn't passed X because ")
                            return 'North'
                        else:
                            print("Z didn't passed Y because")
                            return 'South'
        elif (deltaY != 0):
            if (deltaY < 0):
                x, y = loc
                y -= 1
                lookUpLoc = (y, x)
                mineLook = (y, x)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                    print("Going Y")
                    return 'South'
                else:
                    y += 1
                    if (deltaX < 0 ):
                        x -= 1
                        lookUpLoc = (y, x)
                        mineLook = (y, x)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            return 'West'
                        else:
                            return 'East'
                    else:
                        x += 1
                        lookUpLoc = (y, x)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            return 'East'
                        else:
                            return 'West'
            else:
                x, y = loc
                y += 1
                lookUpLoc = (y, x)
                mineLook = (y,x)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                    print lookUpLoc
                    print("Going North")
                    return 'North'
                else:
                    y -= 1
                    if (deltaX < 0 ):
                        x -= 1
                        lookUpLoc = (y, x)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            return 'West'
                        else:
                            return 'East'
                    else:
                        x += 1
                        lookUpLoc = (y, x)
                        mineLook = (y,x)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs))):
                            return 'East'
                        else:
                            return 'West'
        else:
            return 'Stay'

    def getMineIsMine(self, myHero, mines_loc, mines_locs):
        return mines_locs[mines_loc] == myHero.id


    def getNearestMine(self, myHero, mines_locs):
        not_owned_mine = []
        for mine in mines_locs.keys():
            if(mines_locs[mine] != myHero.id):
                not_owned_mine.append(mine)

        deltaX = 999999
        deltaY = 999999

        for mine_position in not_owned_mine:
            distance_calculated = self.distance(myHero.pos, mine_position)

            if(deltaX + deltaY > distance_calculated[0] + distance_calculated[1]):
                deltaY = distance_calculated[0]
                deltaX = distance_calculated[1]
                self.wantedPosition = distance_calculated

        print (deltaY, deltaX)
        return (deltaY, deltaX)

    def distance(self, pos1, pos2):
        y = (pos2[1] - pos1["y"])
        x = (pos2[0] - pos1["x"])
        return (y,x)

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'East', 'West', 'South', 'North']
        return choice(dirs)

