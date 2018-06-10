class GameBoard:
    def __init__(self, x: int, y: int) -> None:
        self.grid = [x]
        for column in x:
            for row in y:
                self.grid[column][row] = Cell()
    
    def birth(self, x: int, y:int) -> None:
        self.grid[x][y].alive_after_tick = True

    def kill(self, x: int, y:int) -> None:
        self.grid[x][y].alive_after_tick = False

    def tick(self) -> None:
        for x in len(self.grid):
            for y in len(self.grid[0]):
                self.grid[x][y].tick()

class Cell:
    def __init__(self) -> None:
        self.alive = False
        self.alive_after_tick = False

    def tick(self) -> None:
        self.alive = self.alive_after_tick

