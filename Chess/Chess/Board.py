from Rook import *
from Bishop import *
from Knight import *
from Queen import *
from King import *
from Pawn import *


WHITE = 1
BLACK = 2


def opponent(color):
    # Удобная функция для вычисления цвета противника
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    # Функция проверяет, что координаты (row, col) 
    # лежат внутри доски
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [Rook(0,0,WHITE), Bishop(0,1,WHITE), Knight(0,2,WHITE), Queen(0,3,WHITE), 
                         King(0,4,WHITE), Knight(0,5,WHITE), Bishop(0,6,WHITE), Rook(0,7,WHITE)]
        self.field[1] = [Pawn(1,0,WHITE), Pawn(1,1,WHITE), Pawn(1,2,WHITE), Pawn(1,3,WHITE), 
                         Pawn(1,4,WHITE), Pawn(1,5,WHITE), Pawn(1,6,WHITE), Pawn(1,7,WHITE)]
        self.field[7] = [Rook(7,0,BLACK), Bishop(7,1,BLACK), Knight(7,2,BLACK), Queen(7,3,BLACK), 
                         King(7,4,BLACK), Knight(7,5,BLACK), Bishop(7,6,BLACK), Rook(7,7,BLACK)]
        self.field[6] = [Pawn(6,0,BLACK), Pawn(6,1,BLACK), Pawn(6,2,BLACK), Pawn(6,3,BLACK), 
                         Pawn(6,4,BLACK), Pawn(6,5,BLACK), Pawn(6,6,BLACK), Pawn(6,7,BLACK)] 

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
        # Возвращает строку из двух символов. Если в клетке (row, col)
        # находится фигура, символы цвета и фигуры. Если клетка пуста,
        # то два пробела.
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        # Переместить фигуру из точки (row, col) в точку (row1, col1).
        # Если перемещение возможно, метод выполнит его и вернёт True.
        # Если нет --- вернёт False

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False

        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку

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

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def can_attack(self, row, col, row1, col1):
        self
