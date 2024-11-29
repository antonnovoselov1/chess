WHITE = 1
BLACK = 2


# ������� ������� ��� ���������� ����� ����������
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board(board):  # ����������� ����� � ��������� ���� (��. ��������)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # ������ ��������� �����
    board = Board()
    # ���� ����� ������ �������
    while True:
        # ������� ��������� ����� �� �����
        print_board(board)
        # ��������� �� ��������
        print('Commands:')
        print('    exit                               -- exit')
        print('    move <row> <col> <row1> <col1>     -- move from (row, col)')
        print('                                          into (row1, col1)')
        # ������� ����������� ������ ������� �����
        if board.current_player_color() == WHITE:
            print('White turn:')
        else:
            print('Black turn:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Succesful move')
        else:
            print('Incorrect coordinates! Try another move!')


def correct_coords(row, col):
    # ������� ���������, ��� ���������� (row, col) 
    # ����� ������ �����
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [Rook(WHITE), Bishop(WHITE), Knight(WHITE), Queen(WHITE), King(WHITE), Knight(WHITE),
                         Bishop(WHITE), Rook(WHITE)]
        self.field[1] = [Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
                         Pawn(WHITE)]
        self.field[0] = [Rook(BLACK), Bishop(BLACK), Knight(BLACK), Queen(BLACK), King(BLACK), Knight(BLACK),
                         Bishop(BLACK), Rook(BLACK)]
        self.field[1] = [Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
                         Pawn(BLACK)]

    def is_under_attack(self, r, c, color):
        for row in range(8):
            for col in range(8):
                if self.field[row][col] != None:
                    if self.field[row][col].get_color() == color:
                        if self.field[row][col].can_move(r, c): return True

        return False

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        # ���������� ������ �� ���� ��������. ���� � ������ (row, col)
        # ��������� ������, ������� ����� � ������. ���� ������ �����,
        # �� ��� �������.
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        # ����������� ������ �� ����� (row, col) � ����� (row1, col1).
        # ���� ����������� ��������, ����� �������� ��� � ����� True.
        # ���� ��� --- ����� False

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False

        if row == row1 and col == col1:
            return False  # ������ ����� � �� �� ������

        piece = self.field[row][col]
        if piece is None:
            return False

        if piece.get_color() != self.color:
            return False

        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False

        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False

        else:
            return False

        self.field[row][col] = None  # ����� ������.
        self.field[row1][col1] = piece  # ��������� �� ����� �����.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def can_attack(self, row, col, row1, col1):
        self


class Pawn:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        # ����� ����� ������ ������ �� ���������
        # "������ �� �������" �� �����������
        if col != col1:
            return False

        # ����� ����� ������� �� ���������� ��������� ��� �� 2 ������
        # �����, ������� �������� ������ ���������� ���� � start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ��� �� 1 ������
        if row + direction == row1:
            return True

        # ��� �� 2 ������ �� ���������� ���������
        if (row == start_row and row + 2 * direction == row1 and board.field[row + direction][col] is None):
            return True
        # if self.row == start_row and self.row + 2 * direction == row:
        #     return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return row + direction == row1 and (col + 1 == col1 or col - 1 == col1)


class Rook:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    # def set_position(self, row, col):
    #     self.row = row
    #     self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        # ���������� ������� ��� � ������, ������� �� ����� � ��� �� ����
        # ��� ������� ������.
        if self.row != row and self.col != col:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # ���� �� ���� �� ��������� ���� ������
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # ���� �� ���� �� ����������� ���� ������
            if not (board.get_piece(row, c) is None):
                return False

        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    # ���������!!!
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


class King:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def char(self):
        return 'K'

    def get_color(self):
        return self.color

    # ���������!!!
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


class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    # ���������!!!
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


if __name__ == "__main__":
    main()