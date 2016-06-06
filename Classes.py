class Board:
    import time

    def __init__(self, size = 10):
        self.size = size
        self.state = [['.'] * size for i in range(size)]

    def drawState(self):
        for row in self.state:
            print ' '.join(row)

    def step(self):
        # implement in inheriting classes
        print "Not implemented"

    def run(self, steps = 0):
        self.drawState()

        for i in range(steps):
            self.step()
            self.drawState()
            time.sleep(1)

class RandomBoard(Board):
    import random

    def step(self):
        
        y = self.random.randrange(0, self.size)
        x = self.random.randrange(0, self.size)
        self.state[y][x] = 'O'