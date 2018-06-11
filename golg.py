class GameOfLife:
    def __init__(self, board: 'GameBoard') -> None:
        self.board = board
    
    def prepare_tick(self) -> None:
        for x in range(self.board.columns):  # Count live neighbours
            for y in range(self.board.rows):  # Loop over every cell
                live_neighbours = 0
                for n_x in range(x-1, x+2):
                    for n_y in range(y-1, y+2):  # Loop over all neighbours
                        # Exclude centre and check for neighbours not in grid
                        if not (n_x == x and n_y == y) and \
                                0 <= n_x < self.board.columns and \
                                0 <= n_y < self.board.rows:
                                        if self.board.grid[n_x][n_y].alive:
                                            live_neighbours += 1

    def start(self) -> None:
        pass

class GameBoard:
    def __init__(self, columns: int, rows: int) -> None:
        self.grid = [[Cell() for column in range(columns)] for row in \
                range(rows)] 
        self.columns = columns
        self.rows = rows

    def birth(self, x: int, y:int) -> None:
        self.grid[x][y].alive_after_tick = True

    def kill(self, x: int, y:int) -> None:
        self.grid[x][y].alive_after_tick = False

    def tick(self) -> None:
        for x in range(self.columns):
            for y in range(self.rows):
                self.grid[x][y].tick()

class Cell:
    def __init__(self) -> None:
        self.alive = False
        self.alive_after_tick = False

    def tick(self) -> None:
        self.alive = self.alive_after_tick

if __name__ == '__main__':
    gb = GameBoard(5, 5)
    gol = GameOfLife(gb)
    gb.birth(2,2)
    gb.birth(2,3)
    gb.tick()
    gol.prepare_tick()
