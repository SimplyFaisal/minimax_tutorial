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

"""
This class stores the move that was made and the resulting utility.
"""
class Result(object):
    """
    Args:

        move: (int) represents the move that was made. 1 = up, 2 = down,
        3 = left, 4 = right.

        utility: (int) THe utility of the resulting state after applying the
        move
    """
    def __init__(self, move=None, utility=None):
        self.move = move
        self.utility = utility

    def __str__(self):
        return '<Result move=%s utility=%s>' % (self.move, self.utility)

class PlayerAI(BaseAI):

    MAX_DEPTH = 14

    """
    Returns a move for the current grid state. This method is called in
    GameManager.py.
    """
    def getMove(self, grid):
        return self.minimax(grid);


    """
    Should implement the minimax algorithm to return a move for the given state.
    """
    def minimax(self, grid):
        return self.random_move(grid)


    """
    Returns a random move for the given grid.
    """
    def random_move(self, grid):
        return random.choice(grid.getAvailableMoves())


    """
    Returns the best move that max can make.
    """
    def max_value(self, grid, depth=None, previous=None):
        """
        1.) Check if the grid is in a terminal state. If it is then return a
        Result object with the utility of the current state and the move that
        caused it.

        2.) Get all the moves that max(our bot in this case) can make. Make sure
        you clone the grid before applying the move.

        3.) For every one of those moves see what min would do.

        4.) Select the move with the highest value.
        """
        pass


    """
    Returns the moves that max can make to the given grid.
    """
    def get_moves_for_max(self, grid):
        pass


    """
    Returns the best move that min can make. You can think of this as the worst
    move min can make to hinder max.
    """
    def min_value(self, grid, depth=None, previous=None):
        """
        1.) Check if the grid is in a terminal state. If it is then return a
        Result object with the utility of the current state and the move that
        caused it.

        2.) Get all the moves that min(our bots adversary) can make. What
        constitutes a "move" for min though? Hint: Remember that a new tile is
        added to the board....
        Like above remember to clone the board before applying the "move".

        3.) For every one of those moves see what max(our bot) would do.

        4.) Select the move with the lowest value.
        """
        pass

    """
    Returns the moves that min can make to the given grid.
    """
    def get_moves_for_min(self, grid):
        pass


    """
    Determines if the grid is in a terminal state. Specifically this method
    terminates there are no legal moves or if the algorithm has decended to
    the maximum depth.

    Args:
        grid: (Grid) The current state of the grid
        depth: (int) the current depth of this branch of the search tree.
    """
    def terminal_test(self, grid, depth):
        return grid.canMove() or depth > self.MAX_DEPTH


    """
    Returns the utility for the current state of the grid. The current
    implementation simply optmizes for the largest value. Can you come up with a
    smarter utility function(or set of utility functions...hint hint :)

    Args:
        grid: (Grid) the current state of the grid.
    """
    def utility(self, grid):
        return max_tile(tile)

    """
    Returns the value of the largest tile in the grid.

    Args:
        grid: (Grid) the current state of the grid.
    """
    def max_tile(self, grid):
        return log2(grid.getMaxTile())


