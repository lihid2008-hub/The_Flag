import pygame
import GameField
import Screen
import Soldier
import consts

state = {
    "soldier_location": consts.START_LOCATION,
    "state": consts.RUNNING_STATE,
    "night_mode": False,
    "grass": [],
    "mine": [],
    "flag": [],
    "exploding": None
}


def main():
    pygame.init()
    GameField.create_game_field(state)

    while state["state"] == consts.RUNNING_STATE:
        handel_user_event()

        #getting soldier locations:
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
            old_location = list(state["soldier_location"])
            row, col = state["soldier_location"]
            new_row, new_col = row, col

            if event.key == pygame.K_RETURN:
                state["night_mode"] = True
                break

            elif event.key == pygame.K_UP and row > 0:
                new_row = row - 1
            elif event.key == pygame.K_DOWN and row + consts.SOLDIER_ROWS <= consts.BOARD_ROWS:
                new_row = row + 1
            elif event.key == pygame.K_LEFT and col > 0:
                new_col = col - 1
            elif event.key == pygame.K_RIGHT and col + consts.SOLDIER_COLS < consts.BOARD_COLS - 1:
                new_col = col + 1

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


if __name__ == '__main__':
    main()
