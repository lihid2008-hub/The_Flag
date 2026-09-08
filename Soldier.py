import consts

def get_soldier(field):
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if field[row][col] == "player":
                return row,col
    return consts.START_LOCATION[0],consts.START_LOCATION[1]