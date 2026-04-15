from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        random_move = random.choice(self.moves)
        # Add random coordinates to current position
        self.position = (random_move[0] + self.position[0], random_move[1] + self.position[1])
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass    

class Pawn(Player):
    def __init__(self):
        super().__init__()
        # Up, Down, Left, Right
        self.moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def level_up(self):
        # 4 additional diagonal moves
        self.moves += [(1, -1), (1, 1), (-1, 1), (-1, -1)]       
