import time

class GameBoard:
    def __init__(self, columns: int, rows: int) -> None:
        self.grid = [[Cell() for column in range(columns)] for row in \
                range(rows)] 
        self.columns = columns
        self.rows = rows

    def display(self) -> None:
        for y in reversed(range(self.rows)):
            for x in range(self.columns):
                if self.grid[x][y].alive:
                    print('x', end ='')
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
                        # Exclude centre and make sure neighbours are in grid
                        if not (n_x == x and n_y == y) and \
                                0 <= n_x < self.columns and \
                                0 <= n_y < self.rows:
                                        if self.grid[n_x][n_y].alive:
                                            live_neighbours += 1
                if cell.alive and live_neighbours <= 1:
                    cell.kill()  # Underpopulation
                elif cell.alive and live_neighbours >= 4:
                    cell.kill()  # Overpopulation
                elif not cell.alive and live_neighbours == 3:
                    cell.birth()  # Birth

    def play(self) -> None:
        while True:
            print()
            self.display()
            self.prepare_tick()
            self.tick()
            time.sleep(1)

class Cell:
    def __init__(self) -> None:
        self.alive = False
        self.alive_after_tick = False

    def birth(self) -> None:
        self.alive_after_tick = True

    def kill(self) -> None:
        self.alive_after_tick = False

    def tick(self) -> None:
        self.alive = self.alive_after_tick

if __name__ == '__main__':
    gb = GameBoard(5, 5)
    gb.grid[3][1].alive = True
    gb.play()
