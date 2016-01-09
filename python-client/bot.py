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
        number_of_mine = self.number_of_mine(game)
        for move in possibleMove:
            pos = game.board.to(loc, move)
            if (game.board.is_mine(pos) and game.mines_locs[pos] != str(game.myHero.id) and game.myHero.life > 25):
                return move
            elif (game.board.is_tavern(loc) and game.myHero.life <= 50):
                return move
            elif (game.board.is_mine(pos) and game.mines_locs[pos] != str(game.myHero.id) and number_of_mine == 0):
                return move
            elif (game.board.passable(pos) and (game.board.is_not_pine(pos) or game.myHero.life >= 25)):
                passables.append(move)


        for passable in passables:
            first_pos = game.board.to(loc, passable)
            for move in possibleMove:
                second_pos = game.board.to(first_pos, move)
                if (game.board.is_mine(second_pos) and game.mines_locs[second_pos] != str(game.myHero.id) and game.myHero.life > 25):
                    self.moveToDo.append(move)
                    self.moveToDo.append(passable)
                elif (game.board.is_tavern(second_pos) and game.myHero.life <= 50):
                    self.moveToDo.append(move)
                    self.moveToDo.append(passable)

        for passable in passables:
            first_pos = game.board.to(loc, passable)
            for move in possibleMove:
                second_pos = game.board.to(first_pos, move)
                for second_move in possibleMove:
                    third_pos = game.board.to(second_pos, second_move)
                    if (game.board.is_mine(third_pos) and game.mines_locs[third_pos] != str(game.myHero.id) and game.myHero.life > 25 ):
                        self.moveToDo.append(second_move)
                        self.moveToDo.append(move)
                        self.moveToDo.append(passable)
                    elif (game.board.is_tavern(third_pos) and game.myHero.life <= 50):
                        self.moveToDo.append(second_move)
                        self.moveToDo.append(move)
                        self.moveToDo.append(passable)
            if (len(self.moveToDo) != 0):
                return self.moveToDo.pop()
        return choice(passables)

    def number_of_mine(self, game):
        number_of_mine = 0
        for mine in game.mines_locs.keys():
            if(game.mines_locs[mine] == str(game.myHero.id)):
                number_of_mine += 1
        return number_of_mine
class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'Eastest', 'East', 'South', 'North']
        return choice(dirs)
