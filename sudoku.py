import random


class InvalidSudokoBoard(Exception):
    """Raised when the board is incorrect in 1 of the following ways:
        -too many rows
        -a row has too many values
        -the values are not integers between 1-9
    """
    pass


class SudokuBoard:

    def __init__(self, board:list[list[int]]=None, difficulty:str='easy'):

        if board is None:
            self.diffficulty = difficulty
            self.board = [[0 for _ in range(0,9)] for _ in range(0,9)]
            self._fill_diagonal()
            self._fill_board()
            self._remove_squares()
        else:
            for row in board:
                if len(row) != 9:
                    raise InvalidSudokoBoard('Board row contains too many values')
                for num in row:
                    if type(num) != int:
                        raise InvalidSudokoBoard(f'All values must be integers, not {repr(num)}')
                    elif not 0 <= num <= 9:
                        raise InvalidSudokoBoard('All values must be integers between 1 and 9')
            if len(board) != 9:
                raise InvalidSudokoBoard('Board contains too many rows')
            self.board = board


    def _remove_squares(self):
        """Once a new board is generated, this method will remove 
        squares according to the desired difficulty level.

        Easy:       32 - 39 given squares
        Medium:     26 - 31 given squares
        Hard:       22 - 25 given squares
        Expert:     17 - 21 given squares
        """
        match self.diffficulty.lower():
            case 'medium':
                start, stop = (26, 32)
            case 'hard':
                start, stop = (22, 26)
            case 'expert':
                start, stop = (17, 22)
            case _:
                start, stop = (32, 40)

        squares_to_remove = 81 - random.randrange(start, stop)
        nums = [num for row in self.board for num in row]

        while squares_to_remove > 0:
            random_index = random.randint(0, len(nums)-1)
            if nums[random_index] == 0:
                continue
            nums[random_index] = 0
            squares_to_remove -= 1
        self.board = [nums[i:i + 9] for i in range(0, len(nums), 9)]

        return


    def _fill_diagonal(self):
        """Fills the diagonal (top-left to bottom-right) 
        of a blank board (all 0s) with the numbers 1, 
        through 9 in random order.
        """
        nums = list(range(1, 10))
        for i in range(0, 9):
            for j in range(0, 9):
                if j == i:
                    num = random.choice(nums)
                    self.board[i][j] = num
                    nums.remove(num)
        return


    def _fill_board(self) -> bool:
        """Populates the board using recursion magick."""
        try:
            row, col = self.find_empty_square()
        except TypeError:
            return True

        for num in random.sample(population=[1, 2, 3, 4, 5, 6, 7, 8, 9], k=9):
            if self.check_valid_move(num, row, col):
                self.board[row][col] = num
                if self._fill_board():
                    return True
                
                self.board[row][col] = 0

        return False


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

        for num in random.sample(population=[1, 2, 3, 4, 5, 6, 7, 8, 9], k=9):
        # for num in range(1, 10):
            if self.check_valid_move(num, row, col):
                self.board[row][col] = num
                if self.solve_board():
                    return True
                
                self.board[row][col] = 0

        return False



    # def solve_board(self) -> bool:
    #     """Solves the board with recursion magick."""
    #     try:
    #         row, col = self.find_empty_square()
    #     except TypeError:
    #         return True

    #     for num in random.sample(population=[1, 2, 3, 4, 5, 6, 7, 8, 9], k=9):
    #     # for num in range(1, 10):
    #         if self.check_valid_move(num, row, col):
    #             self.board[row][col] = num
    #             if self.solve_board():
    #                 return True
                
    #             self.board[row][col] = 0

    #     return False


