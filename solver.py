import sys


class InvalidSudokoBoard(Exception):
    """Raised when a board is not 9x9"""
    pass


# class NoSolutionPossible(Exception):
#     """Raised when the puzzle does not have any valid solutions."""
#     pass


class SudokuBoard:

    def __init__(self, board:list[list[int]]):
        for row in board:
            if len(row) != 9:
                raise InvalidSudokoBoard('Board row contains too many values')
            for num in row:
                if type(num) != int:
                    raise InvalidSudokoBoard(f'All values must be integers, not {repr(num)}')
                elif not 0 <= num <= 9:
                    print(num)
                    raise InvalidSudokoBoard('All values must be integers between 1 and 9')
        if len(board) != 9:
            raise InvalidSudokoBoard('Board contains too many rows')
        self.board = board


    def _column(self, col_index:int) -> list[int]:
        """Returns a column at a given index position"""
        return [self.board[i][col_index] for i in range(0,9)]


    def _3x3(self, row_index:int, col_index:int) -> list[int]:
        """Get the 3x3 block these coordinates belong to."""
        box = []
        for i in range(0, 3):
            for j in range(0, 3):
                box.append(self.board[row_index//3*3 + i][col_index//3*3 + j])
        return box


    def _check_row(self, num:int, row_index) -> bool:
        """Check if a number is already in a given row."""
        if num in self.board[row_index]:
            return False
        return True


    def _check_col(self, num:int, col_index:int) -> bool:
        """Check if a number is already in a given column."""
        if num in self._column(col_index):
            return False
        return True


    def _check_3x3(self, num:int, row_index:int, col_index:int) -> bool:
        """Check if the number is already in the 3x3 box."""
        if num in self._3x3(row_index, col_index):
            return False
        return True


    def check_valid_move(self, num:int, row_index:int, col_index:int) -> bool:
        """Checks if the number can be placed in this square by 
        checking the row, column, and 3x3 box.
        """
        return bool(self._check_row(num, row_index) 
                    and self._check_col(num, col_index) 
                    and self._check_3x3(num, row_index, col_index)
                    )


    def find_empty_square(self) -> tuple[int] | None:
        """Finds the first empty square"""
        for i in range(0, 9):
            for j in range(0,9):
                if self.board[i][j]  == 0:
                    return (i, j)


    def solve_board(self) -> bool:
        """Solves the board with recursion magick."""
        try:
            row, col = self.find_empty_square()
        except TypeError:
            return True

        for num in range(1, 10):
            if self.check_valid_move(num, row, col):
                self.board[row][col] = num
                if self.solve_board():
                    return True
                
                self.board[row][col] = 0

        return False



def sudoku_solver(puzzle:list[list[int]]):

    try:
        board = SudokuBoard(puzzle)
    except InvalidSudokoBoard as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    if board.solve_board():
        return "Solved"
    
    return "No valid solution possible"



input1 = [
    [0, 0, 6, 1, 0, 0, 0, 0, 8], 
    [0, 8, 0, 0, 9, 0, 0, 3, 0], 
    [2, 0, 0, 0, 0, 5, 4, 0, 0], 
    [4, 0, 0, 0, 0, 1, 8, 0, 0], 
    [0, 3, 0, 0, 7, 0, 0, 4, 0], 
    [0, 0, 7, 9, 0, 0, 0, 0, 3], 
    # [0, 0, 8, 4, 0, 4, 0, 0, 6], 
    [0, 0, 8, 4, 0, 0, 0, 0, 6], 
    [0, 2, 0, 0, 5, 0, 0, 8, 0], 
    [1, 0, 0, 0, 0, 2, 5, 0, 0],
]


print(sudoku_solver(input1))





