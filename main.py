import pygame
import GameField
import Screen
import Soldier
import consts
import random

state = {
    "soldier_location": consts.START_LOCATION,
    "state": consts.RUNNING_STATE,
    "is_running": True,
    "night_mode": False,
    "grass": [],
    "mine": [],
    "flag": []
}


def main():
    pygame.init()
    GameField.create_game_field(state)
    grass = GameField.append_grass()
    state["grass"] = grass
    num = random.randint(0, consts.MINE_ROWS - 1)
    print(num)
    while state["state"] == consts.RUNNING_STATE:

        handel_user_event()
        legs_solider_location = Soldier.get_soldier_legs(GameField.game_field)
        body_soldier_location = Soldier.get_soldier_body(GameField.game_field)

        if is_lose(legs_solider_location):
            state["state"] = consts.LOSE_STATE

        if is_win(body_soldier_location):
            state["state"] = consts.WIN_STATE

        Screen.darw_game(state)

def handel_user_event():
    global row, col
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            old_location = list(state["soldier_location"])
            row, col = state["soldier_location"]
            new_row, new_col = row, col
            if event.key == pygame.K_UP and row > 0:
                new_row = row - 1
            elif event.key == pygame.K_DOWN and row + consts.SOLDIER_ROWS <= consts.BOARD_ROWS:
                new_row = row + 1
            elif event.key == pygame.K_LEFT and col > 0:
                new_col = col - 1
            elif event.key == pygame.K_RIGHT and col + consts.SOLDIER_COLS < consts.BOARD_COLS - 1:
                new_col = col + 1
            elif event.key==pygame.K_RETURN:
                state["night_mode"] = True
                return

            new_location = [new_row, new_col]
            if new_location != old_location:
                state["soldier_location"] = new_location
                GameField.update_soldier_position(old_location, new_location)


def is_win(body_solider_location):
    for i in range(len(body_solider_location)):
        if body_solider_location[i] in state["flag"]:
            return True
    return False


def is_lose(legs_solider_location):
    for i in range(len(legs_solider_location)):
        if legs_solider_location[i] in state["mine"]:
            return True
    return False


if __name__ == '__main__':
    main()
