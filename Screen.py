import GameField
import Soldier
import pygame
import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_soldier(location):
    soldier = pygame.image.load(consts.SOLDIER_IMAGE_PATH)
    x_position, y_position = GameField.get_location_on_field(location[0], location[1])
    new_dimensions = (consts.SOLDIER_ROWS * consts.CELL_SIZE, consts.SOLDIER_COLS * consts.CELL_SIZE)
    resize_image = pygame.transform.scale(soldier, new_dimensions)
    screen.blit(resize_image, (x_position, y_position))

    text_location = ((consts.SOLDIER_COLS + consts.SOLDIER_COLS) * consts.CELL_SIZE, consts.START_LOCATION[1])
    draw_message(consts.START_TEXT, consts.TEXT_FONT_SIZE, consts.START_TEXT_COLOR, text_location)

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_grass(grass):
    grass_pic = pygame.image.load(consts.GRASS_IMAGE_PATH)
    new_dimensions = (consts.BUSH_ROWS * consts.CELL_SIZE,
                      consts.BUSH_COLS * consts.CELL_SIZE)
    resize_image = pygame.transform.scale(grass_pic, new_dimensions)
    for place in grass:
        x_position, y_position = GameField.get_location_on_field(place[0],
                                                                 place[1])
        screen.blit(resize_image, (x_position, y_position))
    pygame.display.flip()

def night_field(game_state):
    screen.fill(consts.NIGHT_BACKGROUND_COLOR)
    pygame.draw.rect(screen, consts.NIGHT_BACKGROUND_COLOR, (200, 150, 100, 50))


def draw_mine(location):
    mine = pygame.image.load(consts.MINE_IMAGE_PATH)
    x_position, y_position = GameField.get_location_on_field(location[0],
                                                             location[1])
    screen.blit(mine, (x_position, y_position))

def draw_lose_message():
    pass


def draw_win_message():
    pass

def darw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_soldier(game_state["soldier_location"])
    # GameField.append_grass()

    if game_state["night_mode"]:
        night_field(game_state)

    elif game_state["state"] == consts.LOSE_STATE:
        draw_lose_message()

    elif game_state["state"] == consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()