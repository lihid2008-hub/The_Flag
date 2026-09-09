import time
import pygame
import GameField
import Screen
import Soldier
import consts
import DataBase

state = {
    "soldier_location": consts.START_LOCATION,
    "state": consts.RUNNING_STATE,
    "night_mode": False,
    "grass": [],
    "mine": [],
    "flag": [],
    "exploding": None,
    "start_press": 0,
    "stop_press": 0,
    "handel_press": {"49": {"save": DataBase.save_in_one,
                           "upload": DataBase.draw_one},
                     "50": {"save": DataBase.save_in_two,
                           "uploud": DataBase.draw_two},
                     "51": {"save": DataBase.save_in_three,
                           "uploud": DataBase.draw_three},
                     "52": {"save": DataBase.save_in_four,
                           "uploud": DataBase.draw_four},
                     "53": {"save": DataBase.save_in_five,
                           "uploud": DataBase.draw_five},
                     "54": {"save": DataBase.save_in_six,
                           "uploud": DataBase.draw_six},
                     "55": {"save": DataBase.save_in_seven,
                           "uploud": DataBase.draw_seven},
                     "56": {"save": DataBase.save_in_eight,
                           "uploud": DataBase.draw_eight},
                     "57": {"save": DataBase.save_in_nine,
                           "uploud": DataBase.draw_nine}
                     }
}

def main():
    pygame.init()
    GameField.create_game_field(state)
    DataBase.open_new_file()

    while state["state"] == consts.RUNNING_STATE:
        handel_user_event()

        # getting soldier locations:
        legs_solider_location = Soldier.get_soldier_legs(GameField.game_field)
        body_soldier_location = Soldier.get_soldier_body(GameField.game_field)

        lose, mine_place = is_lose(legs_solider_location)

        if lose:
            state["state"] = consts.LOSE_STATE
            music_lose()
            state["exploding"] = mine_place[0]

        if is_win(body_soldier_location):
            state["state"] = consts.WIN_STATE
            music_win()

        Screen.darw_game(state)


def handel_user_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            state["start_press"] = time.time()
            old_location = list(state["soldier_location"])
            row, col = state["soldier_location"]
            new_row, new_col = row, col

            if event.key == pygame.K_RETURN:
                state["night_mode"] = True
                break

            elif event.key == pygame.K_UP and row > 0:
                new_row = row - 1
            elif event.key == pygame.K_DOWN and row + consts.SOLDIER_ROWS < consts.BOARD_ROWS:
                new_row = row + 1
            elif event.key == pygame.K_LEFT and col > 0:
                new_col = col - 1
            elif event.key == pygame.K_RIGHT and col + consts.SOLDIER_COLS < consts.BOARD_COLS - 1:
                new_col = col + 1

            new_location = [new_row, new_col]
            if new_location != old_location:
                state["soldier_location"] = new_location
                GameField.update_soldier_position(old_location, new_location)

        keys = [int(key) for key in state["handel_press"].keys()]
        if event.type == pygame.KEYUP and event.key in keys:
            state["stop_press"] = time.time()
            handel_database(event.key)


def is_win(body_solider_location):
    for i in range(len(body_solider_location)):
        if body_solider_location[i] in state["flag"]:
            return True
    return False


def is_lose(legs_solider_location):
    for leg in legs_solider_location:
        for mine in state["mine"]:
            if leg in mine:
                return True, mine
    return False, None


def music_lose():
    pygame.mixer.music.load(consts.LOSE_SOUND)
    pygame.mixer.music.play(loops=0, start=0.8, fade_ms=100)


def music_win():
    pygame.mixer.music.load(consts.WIN_SOUND)
    pygame.mixer.music.play(loops=0, start=0.8, fade_ms=100)


def handel_database(k):
    if state["stop_press"] - state["start_press"] < consts.PRESS_SECONDS:
        state["handel_press"][str(k)]["save"](state)
    else:
        state["handel_press"][str(k)]["upload"](state)


if __name__ == '__main__':
    main()
