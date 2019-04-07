from BaseAI import BaseAI
import Grid
import math
import time
import random

inf = float('Inf')

def log2(x):
    if x == 0:
        return 0
    return math.log(x, 2)

class Result(object):

    def __init__(self, move=None, utility=None):
        self.move = move
        self.utility = utility

    def __str__(self):
        return '<Result move=%s utility=%s>' % (self.move, self.utility)

class PlayerAI(BaseAI):

    MAX_DEPTH = 14
    # the actual time limit is 0.2 but we set it lower so we have time to
    # return a result
    TIME_LIMIT = 0.18

    def getMove(self, grid):
        return self.alpha_beta_search(grid);

    def alpha_beta_search(self, grid):
        return random.choice(self.get_moves_for_max(grid))

    def max_value(self, grid, alpha=None, beta=None, depth=None, previous=None):
        pass

    def min_value(self, grid, alpha=None, beta=None, depth=None, previous=None):
        pass

    def terminal_test(self, grid, depth):
        if time.clock() - self.start_time > self.TIME_LIMIT:
            return True
        if not grid.canMove():
            return True
        return depth > self.MAX_DEPTH

    def utility(self, grid):
        pass

    def get_moves_for_max(self, grid):
        return grid.getAvailableMoves()


