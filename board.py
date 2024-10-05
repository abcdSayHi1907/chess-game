from const_val import *
from square import Square
from piece import *
from move import Move
class Board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    
    def calc_moves(self, piece, row, col):

        # def pawn_moves():
        #     steps = 1 if piece.moved else 2
        #     start = row + piece.dir
        #     end = row + (piece.dir * (1+steps))

        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for move in possible_moves:
                move_row, move_col = move
                if Square.in_range(move_row, move_col):
                    if self.squares[move_row][move_col].empty_or_rival(piece.color):
                        #create square cho new move
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        #create new move
                        move = Move(initial, final)
                        piece.add_move(move)

        if piece.name == 'pawn':
            pass
        elif piece.name == 'knight':
            knight_moves()
        elif piece.name == 'bishop':
            pass
        elif piece.name == 'rook':
            pass
        elif piece.name == 'queen':
            pass
        elif piece.name == 'king':
            pass

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col, )

    def _add_pieces(self, color):
        if color == 'white':
            row_pawn, row_other = (6,7)    
        else:
            row_pawn, row_other = (1,0) 
        #pawn
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn,col, Pawn(color))
        #knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        #bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))


