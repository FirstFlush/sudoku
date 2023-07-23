from copy import deepcopy
import sudoku


# single solution
input1 = [
    [0, 0, 6, 1, 0, 0, 0, 0, 8], 
    [0, 8, 0, 0, 9, 0, 0, 3, 0], 
    [2, 0, 0, 0, 0, 5, 4, 0, 0], 
    [4, 0, 0, 0, 0, 1, 8, 0, 0], 
    [0, 3, 0, 0, 7, 0, 0, 4, 0], 
    [0, 0, 7, 9, 0, 0, 0, 0, 3], 
    [0, 0, 8, 4, 0, 0, 0, 0, 6], 
    [0, 2, 0, 0, 5, 0, 0, 8, 0], 
    [1, 0, 0, 0, 0, 2, 5, 0, 0],
]

# multiple solutions
input2 = [
    [9, 0, 3, 0, 0, 0, 0, 5, 0],
    [0, 0, 8, 0, 0, 0, 3, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [2, 0, 7, 0, 0, 0, 1, 4, 8],
    [0, 6, 1, 0, 4, 0, 9, 0, 0],
    [0, 9, 4, 2, 7, 0, 0, 6, 0],
    [4, 2, 5, 3, 0, 6, 8, 7, 0],
    [0, 0, 6, 9, 5, 0, 4, 3, 0],
    [0, 0, 9, 0, 0, 0, 0, 1, 5],
]



def is_single_solution(iterations:int=50, board:list[list[int]]=None, difficulty:str='easy'):

    solutions = set()
    if board is None:
        sb = sudoku.SudokuBoard(difficulty=difficulty)
    else: 
        sb = board
    for i in range(iterations):
        sb_copy = deepcopy(sb)
        print(f'solving #{i}....')
        sb_copy.solve_board()
        solutions.add(''.join([ str(num) for row in sb_copy.board for num in row]))

    for solution_str in solutions:
        solution = [list(solution_str[i*9 : i*9 + 9]) for i in range(0, 9)]
        for row in solution:
            print([int(num) for num in row])
        print()
        print()

    print('Original puzzle:')
    for row in sb.board:
        print(row)

    print()
    print('Unique solutions:', len(list(solutions)))
    print()

is_single_solution()

# sb = sudoku.SudokuBoard(board=input2)
# sb.solve_board()
# for row in sb.board:
#     print(row)