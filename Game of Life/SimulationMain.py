import pygame as p
import Cell
import random as randy
import Button


WORLD_SIZE = 600  # size of the display
ROWS = COLS = 20  # number of cells per row and column
SQ_WIDTH = WORLD_SIZE // COLS  # width of each cell
clockSpeed = 1  # speed of the clock


def main():
    global screenMain
    screenMain = p.display.set_mode((WORLD_SIZE, WORLD_SIZE+50))  # creates a 600 by 650 window
    clock = p.time.Clock()  # creates a clock
    global clockSpeed

    labels = ['START', 'STOP', 'FASTER', 'SLOWER', 'RESET']
    colors = ['green', 'white', 'lightblue', 'red', 'yellow']
    drawButtons(screenMain, labels, colors)


    aliveCells = []
    num = randy.randint(50, 100)
    for i in range(num):
        aliveCells.append((randy.randint(0, ROWS), randy.randint(0, COLS)))
    world = initializeWorld(aliveCells)
    calculateNeighbors(world)
    updateWorld(world)
    newGeneration(world)
    drawWorld(screenMain, world)

    drawButtons(screenMain, labels, colors)

    p.display.flip()  # update the display
    throw = False  # whether or not to update the cells
    done = False
    while not done:  # repeats this while loop
        for event in p.event.get():
            if event.type == p.QUIT:  # if the window is closed, the program will end
                done = True
            elif event.type == p.MOUSEBUTTONDOWN:  # if the mouse is clicked
                clicked = p.mouse.get_pos()
                if clicked[1] >= 600 and clicked[0] < 120:  # if the start button is clicked, start the program
                    throw = True
                elif clicked[1] >= 600 and clicked[0] < 240:  # if the stop button is clicked, stop the program
                    throw = False
                elif clicked[1] >= 600 and clicked[0] < 360:  # if the faster button is clicked, speed up the program
                    clockSpeed += 0.25
                elif clicked[1] >= 600 and clicked[0] < 480:  # if the slower button is clicked, slow down the program
                    if clockSpeed - 0.25 >= 0.26:
                        clockSpeed -= 0.25
                elif clicked[1] >= 600 > clicked[0]:  # if the reset button is clicked, reset the program
                    aliveCells = []
                    num = randy.randint(50, 100)
                    for i in range(num):  # generate random alive cells
                        aliveCells.append((randy.randint(0, ROWS), randy.randint(0, COLS)))
                    world = initializeWorld(aliveCells)  # creates the cells and puts them into a list called world
                    calculateNeighbors(world)  # finds the alive neighboring cells of each cell

        if throw:  # if the program is running
            updateWorld(world)  # finds what each cell will become next generation
            newGeneration(world)  # creates the next generation of cells
            drawWorld(screenMain, world)  # draws the new generation of cells
            drawButtons(screenMain, labels, colors)  # draws buttons
            p.display.flip()  # update the display
        clock.tick(clockSpeed)  # how fast the program should run
    p.quit()


def initializeWorld(aliveCellCoordinates):
    world = []
    for row in range(ROWS):
        world.append([])
        for col in range(COLS):
            if (col, row) in aliveCellCoordinates:
                world[row].append(Cell.Cell(True))
            else:
                world[row].append(Cell.Cell(False))
    return world


def drawWorld(screen, world):
    for row in range(ROWS):
        for col in range(COLS):
            if world[row][col].isAlive:
                color = 'PaleGreen4'
            else:
                color = 'gray'
            p.draw.rect(screen, color, (col * SQ_WIDTH, row * SQ_WIDTH, SQ_WIDTH, SQ_WIDTH))


def updateWorld(world):
    for r in world:  # for each cell
        for c in r:
            c.update()  # find what the next move will be


def newGeneration(world):
    for r in world:
        for c in r:  # for each cell
            c.nextGeneration()  # make the next generation this generation


def calculateNeighbors(world):
    for r in range(ROWS):  # for each cell
        for c in range(COLS):
            currentCell = world[r][c]
            neighboringCoords = [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),  # all the neighbors of a cell
                                 (c - 1, r),                 (c + 1, r),
                                 (c - 1, r + 1), (c, r + 1), (c + 1, r + 1)]
            for coord in neighboringCoords:
                if coord[0] in range(COLS) and coord[1] in range(ROWS):  # if the cell is alive
                    currentCell.neighbors.append(world[coord[1]][coord[0]])  # add it to this cells neighbor list


def drawButtons(screen, labels, colors):
    for i in range(len(labels)):
        but = Button.Button(labels[i], colors[i], i, screen)
        but.drawButton()
    return


if __name__ == "__main__":
    main()
