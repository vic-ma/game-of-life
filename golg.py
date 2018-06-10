class GameBoard:
    def __init__(self, x: int, y: int) -> None:
        pass
    
    def birth(self, x: int, y:int) -> None:
        pass

    def kill(self, x: int, y:int) -> None:
        pass

    def tick(self) -> None:
        pass

class Cell:
    def __init__(self) -> None:
        self.alive = False
        self.alive_after_tick = False

    def tick(self) -> None:
        self.alive = self.alive_after_tick

