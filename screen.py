import pygame
import consts
from gamefield import game_field

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_soldier(soldier,png =consts.SOLDIER_PNG ):
    soldier_img = pygame.image.load(png)
    sized = pygame.transform.scale(soldier_img,(consts.SOLDIER_WIDTH*2,consts.SOLDIER_HEIGHT))

    screen.blit(sized,(soldier["x"],soldier["y"]))

def draw_bushes():
    bush_img = pygame.image.load(consts.BUSH_PNG)
    bush_img = pygame.transform.scale(bush_img,(60,60))
    for bush in range(20):
        screen.blit(bush_img,(consts.bush_lst[bush][1]*20,consts.bush_lst[bush][0]*20))

def draw_mines():
    mine = pygame.image.load(consts.MINE_PNG)
    mine_img = pygame.transform.scale(mine,(consts.MINE_COLS*20,consts.MINE_ROWS*20))
    for row in range(consts.BOARD_ROWS):
        for col in range(1,consts.BOARD_COLS-1):
            if game_field[row][col] == game_field[row][col-1] == game_field[row][col+1] == consts.MINE_TILE:
                screen.blit(mine_img,(col*20,row*20))

def draw_grid():
    screen.fill("black")
    for row in range(consts.BOARD_COLS):
        for col in range(consts.BOARD_ROWS):
            pygame.draw.rect(screen,(41, 70, 38),(20*row,20*col,20,20),width=1)

def draw_explosion():
    pass

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_welcome():
    draw_message(consts.WELCOME_MESSAGE,consts.WELCOME_FONT_SIZE,consts.WELCOME_COLOR,consts.WELCOME_LOCATION)

def draw_lose():
    draw_message(consts.LOSE_MESSAGE,consts.LOSE_FONT_SIZE,consts.WELCOME_COLOR,consts.LOSE_LOCATION)

def draw_win():
    draw_message(consts.WIN_MESSAGE,consts.WIN_FONT_SIZE,consts.WIN_COLOR,consts.WIN_LOCATION)

def draw_flag():
    flag_img = pygame.image.load(consts.FLAG_PNG)
    flag_img = pygame.transform.scale(flag_img,(consts.FLAG_COLS*20,consts.FLAG_ROWS*20))

    screen.blit(flag_img,(consts.flag_col*20,consts.flag_row*20))

def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_soldier(state["soldier"])
    draw_flag()
    draw_welcome()
    draw_bushes()

    if state["state"] == consts.SHOW_MINES_STATE:
        draw_grid()
        draw_flag()
        draw_soldier(state["soldier"],consts.NIGHT_SOLD_PNG)
        draw_mines()
        pygame.display.flip()
        pygame.time.delay(1000)
        state["state"] = consts.RUNNING_STATE

    if state["state"] == consts.WIN_STATE:
        draw_win()

    if state["state"] == consts.LOSE_STATE:
        screen.fill("red")
        draw_lose()

    pygame.display.flip()