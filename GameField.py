import consts
import random

game_field = []

#A function that generates the field matrix
def create_game_field(state):
    global game_field
    game_field= [[consts.FREE for _ in range(consts.BOARD_COLS)] for _ in
                  range(consts.BOARD_ROWS)]
    add_solider()
    state["flag"] = add_flag()
    state["mine"] = mine_laying()

#A function that adds a soldier
def add_solider():
    for i in range(consts.SOLDIER_ROWS):
        for j in range(consts.SOLDIER_COLS):
            game_field[i][j] = consts.PLAYER

#A function that adds a flag
def add_flag():
    flag = []
    for i in range(consts.BOARD_ROWS-consts.FLAG_ROWS,consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS-consts.FLAG_COLS,consts.BOARD_COLS):
            game_field[i][j] = consts.FLAG
            flag.append([i, j])
    return flag

#Function that checks if a location is empty
def is_free(row, col):
    for i in range(row, row + consts.MINE_ROWS):
        for j in range(col, col + consts.MINE_COLS):
            if game_field[i][j] != consts.FREE:
                return False
    return True

#A function that adds 20 bombs to the field at random locations.
def mine_laying():
    mines = []
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
                mines.append([k, b])
    return mines
#Adds bushes at 20 random locations.
def append_grass():
    grass = []
    max_row = consts.BOARD_ROWS - consts.BUSH_ROWS
    max_col = consts.BOARD_COLS - consts.BUSH_COLS

    for i in range(consts.BUSHES_COUNT):
        while True:
            row = random.randint(0, max_row)
            col = random.randint(0, max_col)
            if is_free(row, col):
                break

        for k in range(row, row + consts.BUSH_ROWS):
            for b in range(col, col + consts.BUSH_COLS):
                game_field[k][b] = consts.MINE
                grass.append([k, b])
    return grass

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
            if i >= consts.BOARD_ROWS or j >= consts.BOARD_COLS or game_field[i][j] == "player":
                return False
    return True

def flag_there(place):
    for i in range(place[0], place[0] + consts.BOARD_ROWS):
        for j in range(place[1], place[1] + consts.BOARD_COLS):
            if i >= consts.BOARD_ROWS or j >= consts.BOARD_COLS or game_field[i][j] == "flag":
                return False
    return True

def get_location_on_field(row, col):
    center_y = consts.CELL_SIZE * row
    center_x = consts.CELL_SIZE * col
    return center_x, center_y


def update_soldier_position(old_location, new_location):
    global game_field
    old_row, old_col = old_location
    for i in range(old_row, old_row + consts.SOLDIER_ROWS):
        for j in range(old_col, old_col + consts.SOLDIER_COLS):
            if 0 <= i < consts.BOARD_ROWS and 0 <= j < consts.BOARD_COLS:
                if game_field[i][j] == consts.PLAYER:
                    game_field[i][j] = consts.FREE

    new_row, new_col = new_location
    for i in range(new_row, new_row + consts.SOLDIER_ROWS):
        for j in range(new_col, new_col + consts.SOLDIER_COLS):
            if 0 <= i < consts.BOARD_ROWS and 0 <= j < consts.BOARD_COLS:
                game_field[i][j] = consts.PLAYER
