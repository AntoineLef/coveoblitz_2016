from random import choice
import time
import math
from game import Game


class Bot:
    def __init__(self):
        self.wantedPosition = 1
        self.moveToDo = []
        self.sightField = 2

    def calculateThreshold(self, Hero, tileNumber, pikeNumber, gettingMine):
        mineCost = 25
        moveCost = 1
        pikeCost = 10
        cost = tileNumber * moveCost + pikeNumber * pikeCost
        if (gettingMine):
            cost = tileNumber * moveCost + pikeNumber * pikeCost + mineCost
        if (Hero.life == 100 and (cost < Hero.life - 20) or (Hero.life >= 35 and (cost < Hero.life - 20))):
            return True
        return False

    def move(self, state):
        game = Game(state)
        if len(self.moveToDo) == 0:
            return self.new_action(game)
        else:
            return self.moveToDo.pop()

    def new_action(self, game):

        loc = (game.myHero.pos["x"], game.myHero.pos["y"])
        possibleMove = ["North", "South", "East", "West"]
        passables = []
        for move in possibleMove:
            pos = game.board.to(loc, move)
            if (game.board.is_mine(pos) and game.mines_locs[pos] != str(game.myHero.id)):
                return move
            elif (game.board.is_tavern(loc) and game.myHero.life <= 50):
                return move

            elif (game.board.passable(pos)):
                passables.append(move)

        for passable in passables:
            first_pos = game.board.to(loc, passable)
            for move in possibleMove:
                second_pos = game.board.to(first_pos, move)
                if (game.board.is_mine(second_pos) and game.mines_locs[second_pos] != str(game.myHero.id)):
                    self.moveToDo.append(move)
                    self.moveToDo.append(passable)
                elif (game.board.is_tavern(second_pos) and game.myHero.life <= 50):
                    self.moveToDo.append(move)
                    self.moveToDo.append(passable)
        if(len(self.moveToDo) != 0):
            return self.moveToDo.pop()


        return choice(passables)


class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'Eastest', 'East', 'South', 'North']
        return choice(dirs)
