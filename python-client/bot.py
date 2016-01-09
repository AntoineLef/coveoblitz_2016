from random import choice
import time
import math
from game import Game

class Bot:

    def __init__(self):
        self.wantedPosition = 1
        self.move_list = []

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
        if len(self.move_list) == 0:
            self.getNearestMine(game.myHero, game.mines_locs)
            self.list_move(game, game.myHero, self.wantedPosition)
            self.move_list.reverse()
        move = self.move_list[0]
        self.move_list.remove(move)

        return move


    def is_this_my_mine(self, mineLookup, game):
        mines = game.mines_locs.keys()

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
                self.wantedPosition = mine_position

        return (deltaX, deltaY)
    pass
    def list_move(self,game,  myHero, wantedPosition):
        print(wantedPosition)
        y, x = wantedPosition
        hero_position = myHero.pos
        deltaX = x - hero_position["x"]
        deltaY = y - hero_position["y"]
        print(deltaX, deltaY)
        while(deltaX !=0 and deltaY != 0):
            print(deltaX, deltaY)
            if(deltaY > 0):
                if(game.board.passable((y + 1, x))):
                    self.move_list.append("North")
                    deltaY -= 1
                elif(game.board.passable((y, x + 1))):
                    self.move_list.append("East")
                    deltaX -= 1
                elif(game.board.passable((y, x - 1))):
                    self.move_list.append("West")
                    deltaX += 1
                else:
                    self.move_list.append("South")
                    deltaY += 1
            elif(deltaY <= 0):
                if(game.board.passable((y - 1, x))):
                    self.move_list.append("North")
                    deltaY -= 1
                elif(game.board.passable((y, x + 1))):
                    self.move_list.append("West")
                    deltaX -= 1
                elif(game.board.passable((y, x - 1))):
                    self.move_list.append("East")
                    deltaX += 1
                else:
                    self.move_list.append("South")
                    deltaY += 1

        print(self.move_list)
        return self.move_list

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

