WHITE = 1
BLACK = 2


class King:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def char(self):
        return 'K'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        valide = [(row +1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1), (row + 1, col),
          (row - 1, col), (row, col + 1), (row, col - 1)]
        
        if ((row1, col1) in valide and correct_coords(row1, col1)) and not (
            board.field[row1][col1] is not None and board.field[row1][col1].color == self.color):
            return True
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
