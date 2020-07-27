#!/usr/bin/env python3

"""
A simple Conway's Game of Life implementation
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import os

GRID_SIZE = 100

# grid = np.zeros((20, 20), dtype=int)
# A glider
# grid[3,3] = 1
# grid[4,4] = 1
# grid[5,4] = 1
# grid[5,3] = 1
# grid[5,2] = 1


def update(grid):
    new_grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            total = int(
                grid[row, (column - 1) % GRID_SIZE]
                + grid[row, (column + 1) % GRID_SIZE]
                + grid[(row - 1) % GRID_SIZE, column]
                + grid[(row + 1) % GRID_SIZE, column]
                + grid[(row - 1) % GRID_SIZE, (column - 1) % GRID_SIZE]
                + grid[(row - 1) % GRID_SIZE, (column + 1) % GRID_SIZE]
                + grid[(row + 1) % GRID_SIZE, (column - 1) % GRID_SIZE]
                + grid[(row + 1) % GRID_SIZE, (column + 1) % GRID_SIZE]
            )

            if grid[row, column] == 1:
                if (total == 2) or (total == 3):
                    new_grid[row, column] = 1
                else:
                    new_grid[row, column] = 0
            if grid[row, column] == 0:
                if total == 3:
                    new_grid[row, column] = 1

    grid[:] = new_grid[:]
    return grid


def run_it(frameNum, grid, img):
    grid = update(grid)
    # print(grid)
    img.set_data(grid)
    return img


def main():
    grid = np.random.randint(2, size=(GRID_SIZE, GRID_SIZE), dtype=int)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation="nearest", aspect="equal")
    # img.set_cmap('hot')  # Black and white
    plt.axis("off")
    plt.axis("image")
    game_animation = animation.FuncAnimation(fig, run_it, fargs=(grid, img), frames=None, interval=1, save_count=50)
    plt.show()


if __name__ == '__main__':
    main()
