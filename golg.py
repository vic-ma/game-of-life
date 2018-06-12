import time
from typing import List

class GameOfLife:
    def __init__(self, columns: int, rows: int) -> None:
        self.grid = [[Cell() for row in range(rows)] for column in
                    range(columns)]
        self.columns = columns
        self.rows = rows

    def display(self) -> None:
        for y in reversed(range(self.rows)):
            for x in range(self.columns):
                if self.grid[x][y].alive:
                    print('*', end ='')
                else:
                    print('o', end ='')
            print()

    def tick(self) -> None:
        for x in range(self.columns):
            for y in range(self.rows):
                self.grid[x][y].tick()

    def prepare_tick(self) -> None:
        for x in range(self.columns):
            for y in range(self.rows):  # Loop over every cell
                cell = self.grid[x][y]
                live_neighbours = 0
                for n_x in range(x-1, x+2):
                    for n_y in range(y-1, y+2):  # Loop over all neighbours
                        if not (n_x == x and n_y == y) and \
                                0 <= n_x < self.columns and \
                                0 <= n_y < self.rows:
                                # If neighbour is not the cell itself and
                                # If neighbour is within grid
                            if self.grid[n_x][n_y].alive:
                                live_neighbours += 1
                if cell.alive and (live_neighbours == 2 or
                                   live_neighbours == 3):
                    cell.live()  # Survival
                elif cell.alive and live_neighbours <= 1:
                    cell.kill()  # Underpopulation
                elif cell.alive and live_neighbours >= 4:
                    cell.kill()  # Overpopulation
                elif not cell.alive and live_neighbours == 3:
                    cell.live()  # Birth


    def play(self) -> None:
        while True:
            print()
            self.display()
            self.prepare_tick()
            self.tick()
            time.sleep(0.5)

    def seed(self, coordinates: List[List[int]]) -> None:
        for coord in coordinates:
            self.grid[coord[0]][coord[1]].alive = True

class Cell:
    def __init__(self) -> None:
        self.alive = False
        self.alive_after_tick = False

    def live(self) -> None:
        self.alive_after_tick = True

    def kill(self) -> None:
        self.alive_after_tick = False

    def tick(self) -> None:
        self.alive = self.alive_after_tick

if __name__ == '__main__':
    gol = GameOfLife(20, 20)
    gol.seed([[10,10],[11,10],[12,10],[12,11],[11,12]])
    gol.play()
