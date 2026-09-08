import consts
import random
import Soldier
import Screen

field = []

def create_field():
    global field
    for i in range(consts.BOARD_ROWS):
        line = []
        for j in range(consts.BOARD_COLS):
            line.append(consts.DEFULT_FIELD)
        field.append(line)
    append_grass()

def append_grass():
    grass = []
    for i in range(consts.BUSHES_COUNT):
        row = random.randint(0, consts.BOARD_ROWS - consts.SOLDIER_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - consts.SOLDIER_COLS - 1)
        grass.append([row, col])

        while not no_grass((row, col), grass):
            row = random.randint(0, consts.BOARD_ROWS - 1)
            col = random.randint(0, consts.BOARD_COLS - 1)

        grass.append([row, col])
    Screen.draw_grass(grass)

def no_grass(place, bushes):
    if soldier_there(place) or flag_there(place):
        return False

    for i in range(place[0], place[0] + consts.BOARD_ROWS):
        for j in range(place[1], place[1] + consts.BOARD_COLS):
            place = [i, j]
            if place in bushes:
                return False
    return True

def soldier_there(place):
    for i in range(place[0], place[0] + consts.SOLDIER_ROWS):
        for j in range(place[1], place[1] + consts.SOLDIER_COLS):
            if i >= consts.BOARD_ROWS or j >= consts.BOARD_COLS or field[i][j] == "player":
                return False
    return True

def flag_there(place):
    for i in range(place[0], place[0] + consts.BOARD_ROWS):
        for j in range(place[1], place[1] + consts.BOARD_COLS):
            if i >= consts.BOARD_ROWS or j >= consts.BOARD_COLS or field[i][j] == "flag":
                return False
    return True

def get_location_on_field(row, col):
    center_y = consts.CELL_SIZE * row
    center_x = consts.CELL_SIZE * col
    return center_x, center_y