#!/usr/bin/python3
""" N queens module """


import sys


def init_board(n):
    """ Initializes a nxn chessboard """
    board = []
    [board.append([]) for i in range(n)]
    [r.append(' ') for i in range(n) for r in board]
    return board


def board_cpy(board):
    """ Returns a copy of the board """
    return [row[:] for row in board]


def solve(board):
    """ Returns a solved chessboard """
    res = []
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 'Q':
                res.append([row, column])
                break
    return res


def elem(board, r, columns):
    """ Eleminates places a queen can not be placed
        args:
            board: The board
            r: The last row that has a queen
            columns: The last column that has a queen """
    for c in range(columns + 1, len(board)):
        board[r][c] = 'x'
    for c in range(columns - 1, -1, -1):
        board[r][c] = 'x'
    for row in range(r + 1, len(board)):
        board[row][columns] = 'x'
    for row in range(r - 1, -1, -1):
        board[row][columns] = 'x'

    c = columns + 1
    for row in range(r + 1, len(board)):
        if c >= len(board):
            break
        board[row][c] = 'x'
        c += 1
    c = columns + 1
    for row in range(r - 1, -1, -1):
        if c >= len(board):
            break
        board[row][c] = 'x'
        c += 1

    c = columns - 1
    for row in range(r - 1, -1, -1):
        if c < 0:
            break
        board[row][c] = 'x'
        c -= 1
    c = columns - 1
    for row in range(r + 1, len(board)):
        if c < 0:
            break
        board[row][c] = 'x'
        c -= 1


def rec_solve(board, r, q, sols):
    """ Solves the puzzle

        args:
            board: The board
            r: The current rows
            q: The number of placed queens
            sols: The list of solutions

        returns:
            The solutions """
    if q == len(board):
        sols.append(solve(board))
        return sols

    for column in range(len(board)):
        if board[r][column] == ' ':
            temp = board_cpy(board)
            temp[r][column] = 'Q'
            elem(temp, r, column)
            sols = rec_solve(temp, r + 1, q + 1, sols)

    return sols


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    b = init_board(n)
    sols = rec_solve(b, 0, 0, [])
    for sol in sols:
        print(sol)
