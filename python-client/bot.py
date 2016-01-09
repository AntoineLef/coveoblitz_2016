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
        deltaX, deltaY = self.getNearestMine(game.myHero, game.mines_locs)
        loc = (game.myHero.pos["x"], game.myHero.pos["y"])
        print( "In move: ",deltaX ,deltaY)
        if (deltaX != 0):
            print ("Not 0 x")
            if (deltaX < 0):
                x, y = loc
                y -= 1
                lookUpLoc = (y, x)
                mineLook = (x, y)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                    print("West passed")
                    return 'West'
                else:
                    if (deltaY < 0 ):
                        x, y = loc
                        x -= 1
                        lookUpLoc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            print ("East didn't pass Y")
                            return 'North'
                        else:
                            print ("East didn't pass X")
                            return 'South'
                    else:
                        x, y = loc
                        x += 1
                        lookUpLoc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            print ("East didn't pass X because deltaY")
                            return 'South'
                        else:
                            print ("East didn't pass Y because deltaY")
                            return 'North'
            else:
                x, y = loc
                y += 1
                lookUpLoc = (y, x)
                mineLook = (x, y)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                    print lookUpLoc
                    print ("Z passed")
                    return 'East'
                else:
                    if (deltaY < 0 ):
                        x, y = loc
                        x -= 1
                        lookUpLoc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            print("Z didn't passed Y")
                            return 'North'
                        else:
                            print("Z didn't passed X")
                            return 'South'
                    else:
                        x, y = loc
                        x += 1
                        loc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(loc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            print("Z didn't passed X because ")
                            return 'South'
                        else:
                            print("Z didn't passed Y because")
                            return 'North'
        elif (deltaY != 0):
            print ("not 0 y")
            if (deltaY < 0):
                x, y = loc
                x -= 1
                lookUpLoc = (y, x)
                mineLook = (x, y)
                print("Looking for mine at ", mineLook)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                    print("Going Y")
                    return 'North'
                else:
                    if (deltaX < 0 ):
                        x, y = loc
                        y -= 1
                        lookUpLoc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            return 'West'
                        else:
                            return 'East'
                    else:
                        x, y = loc
                        y += 1
                        lookUpLoc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            return 'East'
                        else:
                            return 'West'
            else:
                x, y = loc
                x += 1
                lookUpLoc = (y, x)
                mineLook = (x, y)
                print("Looking for mine at ", mineLook)
                print ("South: ", lookUpLoc)
                if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                    print lookUpLoc
                    print("Going North")
                    deltaY +=1
                    return 'South'
                else:
                    if (deltaX < 0 ):
                        x, y = loc
                        y -= 1
                        lookUpLoc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            return 'West'
                        else:
                            return 'East'
                    else:
                        x, y = loc
                        y += 1
                        lookUpLoc = (y, x)
                        mineLook = (x, y)
                        if (game.board.passable(lookUpLoc) or (game.mines_locs.has_key(mineLook) and not self.getMineIsMine(game.myHero, mineLook, game.mines_locs)) or (self.wantedPosition == mineLook)):
                            return 'East'
                        else:
                            return 'West'
        else:
            return 'Stay'

    def getMineIsMine(self, myHero, mines_loc, mines_locs):
        print (mines_locs[mines_loc] == myHero.id)
        return mines_locs[mines_loc] == myHero.id


    def getNearestMine(self, myHero, mines_locs):
        not_oEastned_mine = []
        for mine in mines_locs.keys():
            if(mines_locs[mine] != myHero.id):
                not_oEastned_mine.append(mine)

        deltaX = 999999
        deltaY = 999999
        relativePosY = 999999
        relativePosX = 999999

        for mine_position in not_oEastned_mine:
            distance_calculated = self.distance(myHero.pos, mine_position)
            distance_absolute = self.distanceAbsolute(myHero.pos, mine_position)
            if(deltaX + deltaY > distance_absolute[0] + distance_absolute[1]):
                deltaY = distance_absolute[0]
                deltaX = distance_absolute[1]
                relativePosY = distance_calculated[0]
                relativePosX = distance_calculated[1]
                self.wantedPosition = distance_calculated

        print (relativePosY, relativePosX)
        return (relativePosY, relativePosX)

    def distance(self, pos1, pos2):
        y = (pos2[1] - pos1["y"])
        x = (pos2[0] - pos1["x"])
        return (y,x)
    def distanceAbsolute(self, pos1, pos2):
        y = abs(pos2[1] - pos1["y"])
        x = abs(pos2[0] - pos1["x"])
        return (y,x)

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'Eastest', 'East', 'South', 'North']
        return choice(dirs)

