#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if it is safe to place a queen
        at the position, False otherwise.
    """

    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens to place.

    Returns:
        list: A list of all valid solutions.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.'] * n for _ in range(n)]
    solutions = []

    def backtrack(row):
        """
        Backtracking function to recursively place queens in each row.

        Args:
            row (int): The current row index to place a queen.
        """
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)

    for solution in solutions:
        print('\n'.join(solution))
        print()

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
