import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)

    def drop_disc(self, col, disc):
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = disc
                return row
        return -1

    def is_full(self):
        return np.all(self.board != 0)

    def get_empty_row(self, col):
        for row in range(6):
            if self.board[row][col] == 0:
                return row
        return -1
