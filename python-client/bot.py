from random import choice
import time
from game import Game


class Bot:
    def __init__(self):
        self.wantedPosition = 1
    def move(self, state):
        game = Game(state)
        game.heroes_locs.keys
        game.mines_locs
        game.spikes_locs
        game.taverns_locs
        self.getNearestMine(game.myHero, game.mines_locs)

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
        return (x,y)

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        return choice(dirs)

