import pygame
import GameField
import Screen
import consts

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
    while state["is_running"]:
        handel_user_event()
        Screen.darw_game(state)


def handel_user_event():
    global row, col
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                row = state["soldier_location"][0]
                col = state["soldier_location"][1]
                if state["soldier_location"][0] > 0:
                    state["soldier_location"] = [row - 1, col]
            #elif event.key == pygame.K_DOWN:
                #if state["soldier_location"][0] < 25:
                   # state["soldier_location"] = [row + 1, col]

            elif event.key == pygame.K_LEFT:
                state["soldier_location"] = [0, 5]

            elif event.key == pygame.K_RIGHT:
                state["soldier_location"] = [5, 0]

            elif event.key == pygame.K_SPACE:
                state["night_mode"] = True


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
