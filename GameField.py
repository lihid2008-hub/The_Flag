import consts

import random

game_field = []


def create_game_field():
    global game_field
    game_field= [[consts.FREE for _ in range(consts.BOARD_COLS)] for _ in
                  range(consts.BOARD_ROWS)]
    add_solider()
    add_flag()
    mine_laying()

def add_solider():
    for i in range(consts.SOLDIER_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = consts.PLAYER

def add_flag():
    for i in range(consts.BOARD_ROWS-consts.FLAG_ROWS,consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS-consts.FLAG_COLS,consts.BOARD_COLS):
            game_field[i][j] = consts.FLAG

def print_field():
    for row in game_field:
        print(row)

def is_free(row, col):
    for i in range(row, row + consts.MINE_ROWS):
        for j in range(col, col + consts.MINE_COLS):
            if game_field[i][j] != consts.FREE:
                return False
    return True

def mine_laying():
    max_row = consts.BOARD_ROWS - consts.MINE_ROWS
    max_col = consts.BOARD_COLS - consts.MINE_COLS

    for i in range(consts.MINES_COUNT):
        while True:
            row = random.randint(0, max_row)
            col = random.randint(0, max_col)
            if is_free(row, col):
                break

        for k in range(row, row + consts.MINE_ROWS):
            for b in range(col, col + consts.MINE_COLS):
               game_field[k][b] = consts.MINE


