import consts
import random
import Soldier
import Screen

field = []

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
            if field[i][j] == "player":
                return False
    return True

def flag_there(place):
    for i in range(place[0], place[0] + consts.BOARD_ROWS):
        for j in range(place[1], place[1] + consts.BOARD_COLS):
            if field[i][j] == "flag":
                return False
    return True

def get_location_on_field():
    row, col = Soldier.get_soldier(field)
    center_y = consts.CELL_SIZE * row
    center_x = consts.CELL_SIZE * col
    return center_x, center_y