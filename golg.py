class GameBoard:
    def __init__(self, x: int, y: int) -> None:
        self.grid = [[Cell() for column in range(x)] for row in range(y)] 

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

if __name__ == '__main__':
    gb = GameBoard(5, 5)
