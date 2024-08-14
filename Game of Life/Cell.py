class Cell:  # cell class
    def __init__(self, alive):
        self.isAlive = alive  # whether the cell is alive or not
        self.neighbors = []  # list of the alive neighboring cells
        self.aliveNextFrame = None  # whether the cell will be alive ore dead next frame

    def update(self):
        count = 0
        for cell in self.neighbors:  # counts the number of values in neighbors
            if cell.isAlive:
                count += 1
        if count < 2:  # if less than 2 alive neighboring cells, this cell dies
            self.aliveNextFrame = False
        elif count == 2 and self.isAlive:  # if the cell has 2 alive neighbors and is currently alive, it will be alive next frame
            self.aliveNextFrame = True
        elif count == 3:
            self.aliveNextFrame = True  # if the cell has 3 alive neighbors, it lives next frame
        else:
            self.aliveNextFrame = False  # else the cell dies next frame

    def nextGeneration(self):
        self.isAlive = self.aliveNextFrame  # what the cell will be next frame
