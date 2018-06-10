class GameOfLife:
    def __init__(self, board: GameBoard) -> None:
        self.board = board
    
    def prepare_tick(self) -> None:
        for x in range(board.columns):
            for y in range(board.rows):
                live_neighbours = 0
                for n_x in range(x-1, x+2):
                    for n_y in range(y-1, y+1):
                        if not (n_x == x and n_y == y):
                            if 0 <= n_x < board.columns && \
                                    0 <= n_y < board.rows

    def start(self) -> None:
        pass

class GameBoard:
    def __init__(self, columns: int, rows: int) -> None:
        self.grid = [[Cell() for column in range(x)] for row in range(y)] 
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
    gb.birth(0, 2)
    gb.tick()
    print(gb.grid[0][2].alive)
