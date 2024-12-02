WHITE = 1
BLACK = 2


class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        valide = [(row + 2, col - 1), (row + 2, col + 1), (row - 2, col - 1), (row - 2, col + 1), (row + 1, col + 2),
                  (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)]
        if ((row1, col1) in valide and correct_coords(row1, col1)) and not (
            board.field[row1][col1] is not None and board.field[row1][col1].color == self.color):
            return True
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
