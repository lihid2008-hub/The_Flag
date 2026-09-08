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
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state["soldier_location"] = [5,5]
            elif event.key == pygame.K_DOWN:
                state["soldier_location"] = [2,5]

            elif event.key == pygame.K_LEFT:
                state["soldier_location"] = [0,5]

            elif event.key == pygame.K_RIGHT:
                state["soldier_location"] = [5,0]

            elif event.key == pygame.K_SPACE:
                state["night_mode"] = True


if __name__ == '__main__':
    main()