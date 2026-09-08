import consts
import random
import Screen

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

def append_grass():
    grass = []
    for i in range(consts.BUSHES_COUNT):
        row = random.randint(0, consts.BOARD_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - 1)

        while not no_grass((row, col), grass):
            row = random.randint(0, consts.BOARD_ROWS - 1)
            col = random.randint(0, consts.BOARD_COLS - 1)
        grass.append((row, col))
        Screen.draw_grass((row, col))

def no_grass(place, bushes):
    if soldier_there(place) or flag_there(place):
        return False

    for i in range(place[0], place[0] + consts.BOARD_ROWS):
        for j in range(place[1], place[1] + consts.BOARD_COLS):
            if (i, j) in bushes:
                return False
    return True

def soldier_there(place):
    for i in range(place[0], place[0] + consts.SOLDIER_ROWS):
        for j in range(place[1], place[1] + consts.SOLDIER_COLS):
            if game_field[i][j] == "player":
                return False
    return True

def flag_there(place):
    for i in range(place[0], place[0] + consts.BOARD_ROWS):
        for j in range(place[1], place[1] + consts.BOARD_COLS):
            if game_field[i][j] == "flag":
                return False
    return True

def get_location_on_field(row, col):
    center_y = consts.CELL_SIZE * row
    center_x = consts.CELL_SIZE * col
    return center_x, center_y
