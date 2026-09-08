import consts

def get_soldier_parts(field):
    body= []
    count = consts.SOLDIER_BODY_ROWS * consts.SOLDIER_COLS
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if count == len(body):
                return body
            elif field[row][col] == "player":
                body.append([row, col])
    return body

def get_soldier_legs(field):
    legs = []
    count = consts.SOLDIER_FEET_ROWS * consts.SOLDIER_COLS
    for row in reversed(range(consts.BOARD_ROWS)):
        for col in reversed(range(consts.BOARD_COLS)):
            if count == len(legs):
                return legs
            elif field[row][col] == "player":
                legs.append([row, col])
    return legs
