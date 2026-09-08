import consts

def get_soldier_parts(field):
    body, legs = [], []
    count = consts.SOLDIER_BODY_ROWS * consts.SOLDIER_COLS
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if count == len(body):
                get_soldier_legs(body)
            elif field[row][col] == "player":
                body.append([row, col])
    return body, legs

