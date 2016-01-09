from random import choice
import time
from game import Game
from game import Hero

class Bot:
    def move(self, state):
        game = Game(state)
        game.heroes_locs.keys
        game.mines_locs
        game.spikes_locs
        game.taverns_locs
        self.getNearestEnemy(game.myHero, game.mines_locs)


    pass

    def getNearestMine(self, myHero, mines_locs):
        mines_locs

    def distance(self, pos1, pos2):
        x = abs(pos2[0] - pos1[0])
        y = abs(pos2[1] - pos1[1])
        return (x,y)




class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

