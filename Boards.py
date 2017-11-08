import copy
import random
"""TODO
    * Object to repesent cells
        - Position
        - State added by children
    * Save history
    * Better draw
    * Read initial state from file
"""

class Board(object):


    def __init__(self, initialState):
        self.state = initialState
        # TODO validate
        self.yLen = len(self.state)
        self.xLen = len(self.state[0])

    def draw(self):
        for row in self.state:
            print ' '.join(row)

    def step(self):
        # TODO check best practice
        # implement in inheriting classes
        print "Not implemented"

    # Step, then draw
    def stepDraw(self):
        # Step, then draw
        self.step()
        self.draw()

    def run(self, steps = 0):
        # TODO tidy
        line = '__' * len(self.state[0])
        print line
        self.draw()
        for i in range(steps):
            print line
            self.stepDraw()
        print line

    def getNeighbours(self, y, x):
        # TODO this is gross
        # Maybe generate a list of index modifier tuples and map over it
        return [
            self.state[(y+1) % self.yLen][x],                 # North
            self.state[(y-1) % self.yLen][x],                 # South
            self.state[y][(x+1) % self.xLen],                 # East
            self.state[y][(x-1) % self.xLen],                 # West
            self.state[(y+1) % self.yLen][(x+1) % self.xLen], # North-East
            self.state[(y+1) % self.yLen][(x-1) % self.xLen], # North-West
            self.state[(y-1) % self.yLen][(x+1) % self.xLen], # South-East
            self.state[(y-1) % self.yLen][(x-1) % self.xLen]  # South-West
        ]


class BinaryBoard(Board):
    # TODO Represent the board as booleans and just use chars to print
    alive = 'O'
    dead = '.'
    defaultSize = 10

    def __init__(self, initialState = None):
        if initialState is None:
            initialState = self.getDefaultInitialState()
        super(BinaryBoard,self).__init__(initialState)

    def getDefaultInitialState(self):
        # TODO polish this
        def createLine():
            return [str(self.dead) for x in range(self.defaultSize)]

        return [createLine() for x in range(defaultSize)]


class Random(BinaryBoard):

    def step(self):
        y = self.random.randrange(0, len(self.state))
        x = self.random.randrange(0, len(self.state[0]))
        self.state[y][x] = self.alive


class GameOfLife(BinaryBoard):

    def getNeighbourCount(self, y, x):
        return self.getNeighbours(y, x).count(self.alive)

    def step(self):
        newState = copy.deepcopy(self.state)
        # TODO abstract the iteration over the board
        for y, row in enumerate(self.state):
            for x, cell in enumerate(row):
                neighbourCount = self.getNeighbourCount(y, x)
                newCell = cell
                if cell == self.dead and neighbourCount == 3:
                    newCell = self.alive
                elif cell == self.alive and (neighbourCount < 2 or neighbourCount > 3):
                    newCell = self.dead
                newState[y][x] = newCell

        self.state = newState

