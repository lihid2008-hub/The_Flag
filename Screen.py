import GameField
import pygame
import consts
import time

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

#region -------------DRAW IMAGES---------------
def draw_soldier(location):
    soldier = pygame.image.load(consts.SOLDIER_IMAGE_PATH)
    x_position, y_position = GameField.get_location_on_field(location[0], location[1])

    #Adjusts the image size to the desired ratio.
    new_dimensions = (consts.SOLDIER_COLS * consts.CELL_SIZE,
                      consts.SOLDIER_ROWS * consts.CELL_SIZE)
    resize_image = pygame.transform.scale(soldier, new_dimensions)
    screen.blit(resize_image, (x_position, y_position))

    text_location = ((consts.SOLDIER_COLS + consts.SOLDIER_COLS) * consts.CELL_SIZE, consts.START_LOCATION[1])
    draw_message(consts.START_TEXT, consts.TEXT_FONT_SIZE, consts.START_TEXT_COLOR, text_location)

def draw_grass(grass):
    grass_pic = pygame.image.load(consts.GRASS_IMAGE_PATH)

    #Adjusts the image size to the desired ratio.
    new_dimensions = (consts.BUSH_COLS * consts.CELL_SIZE,
                      consts.BUSH_ROWS * consts.CELL_SIZE)

    resize_image = pygame.transform.scale(grass_pic, new_dimensions)
    for place in grass[::consts.BUSH_COLS]:
        x_position, y_position = GameField.get_location_on_field(place[0], place[1])
        screen.blit(resize_image, (x_position, y_position))

def draw_night_soldier(location):
    soldier = pygame.image.load(consts.SOLDIER_NIGHT_IMAGE_PATH)

    #Adjusts the image size to the desired ratio.
    x_position, y_position = GameField.get_location_on_field(location[0],
                                                             location[1])
    new_dimensions = (consts.SOLDIER_COLS * consts.CELL_SIZE,
                      consts.SOLDIER_ROWS * consts.CELL_SIZE)
    resize_image = pygame.transform.scale(soldier, new_dimensions)
    screen.blit(resize_image, (x_position, y_position))

def draw_flag(location):
    flag = pygame.image.load(consts.FLAG_IMAGE_PATH)
    x_position, y_position = GameField.get_location_on_field(location[0],
                                                             location[1])

    #Adjusts the image size to the desired ratio.
    new_dimensions = (consts.FLAG_COLS * consts.CELL_SIZE,
                      consts.FLAG_ROWS * consts.CELL_SIZE)
    resize_image = pygame.transform.scale(flag, new_dimensions)

    screen.blit(resize_image, (x_position, y_position))

def draw_mine(mines):
    mine_pic = pygame.image.load(consts.MINE_IMAGE_PATH)

    #Adjusts the image size to the desired ratio.
    new_dimensions = (consts.MINE_COLS * consts.CELL_SIZE,
                      consts.MINE_ROWS * consts.CELL_SIZE)

    resize_image = pygame.transform.scale(mine_pic, new_dimensions)

    for mine in mines:
        place = mine[0]
        x_position, y_position = GameField.get_location_on_field(place[0],
                                                                 place[1])
        screen.blit(resize_image, (x_position, y_position))

def draw_injury_soldier(location):
    soldier = pygame.image.load(consts.INJURY_IMAGE_PATH)
    x_position, y_position = GameField.get_location_on_field(location[0],
                                                             location[1])

    # Adjusts the image size to the desired ratio.
    new_dimensions = (consts.SOLDIER_COLS * consts.CELL_SIZE,
                      consts.SOLDIER_ROWS * consts.CELL_SIZE)
    resize_image = pygame.transform.scale(soldier, new_dimensions)
    screen.blit(resize_image, (x_position, y_position))

def draw_explode_mine(place):
    explode_pic = pygame.image.load(consts.EXPLOSION_IMAGE_PATH)

    # Adjusts the image size to the desired ratio.
    new_dimensions = (consts.BUSH_COLS * consts.CELL_SIZE,
                              consts.BUSH_ROWS * consts.CELL_SIZE)

    resize_image = pygame.transform.scale(explode_pic, new_dimensions)

    x_position, y_position = GameField.get_location_on_field(place[0], place[1])
    screen.blit(resize_image, (x_position, y_position))
#endregion

#region----------NIGHT MODE------------
#When the player presses Enter, the bomb locations will be printed on the screen.
def night_field(game_state):
    screen.fill(consts.NIGHT_BACKGROUND_COLOR)
    draw_grid_rects()
    draw_night_soldier(game_state["soldier_location"])
    draw_mine(game_state["mine"])
    pygame.display.flip()
    time.sleep(consts.SHOW_NIGHT_TIME)

#Draws the grid of the board
def draw_grid_rects():
    block_size = consts.CELL_SIZE
    for x in range(0, consts.WINDOW_WIDTH, block_size):
        for y in range(0, consts.WINDOW_HEIGHT,block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, consts.LINE_COLOR, rect, 1)
#endregion

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
    pygame.display.flip()
    time.sleep(consts.SHOW_LOSE_TIME)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)
    pygame.display.flip()
    time.sleep(consts.SOW_WIN_TIME)

def darw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_flag(game_state["flag"][0])
    draw_grass(game_state["grass"])

    if game_state["state"] == consts.LOSE_STATE:
        draw_injury_soldier(game_state["soldier_location"])
        draw_explode_mine(game_state["exploding"])
        draw_lose_message()

    else:
        draw_soldier(game_state["soldier_location"])

        if game_state["state"] == consts.WIN_STATE:
            draw_win_message()

        elif game_state["night_mode"]:
            night_field(game_state)
            game_state["night_mode"] = False
    pygame.display.flip()
