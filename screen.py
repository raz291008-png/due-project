import pygame
import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_soldier(soldier):
    soldier_img = pygame.image.load(consts.SOLDIER_PNG)
    sized = pygame.transform.scale(soldier_img,(consts.SOLDIER_WIDTH*2,consts.SOLDIER_HEIGHT))

    screen.blit(sized,(soldier["x"],soldier["y"]))

def draw_mines():
    pass

def draw_grid():
    grid_img = pygame.image.load(consts.GRID_PNG)
    grid_img = pygame.transform.scale(grid_img,(consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

    screen.blit(grid_img,(0,0))

def draw_explosion():
    pass

def welcome_msg():
    pass

def draw_flag():
    pass

def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_soldier(state["soldier"])
    draw_flag()
    welcome_msg()

    # if state["state"] == consts.SHOW_MINES_STATE:
    screen.fill("black")
    draw_mines()
    draw_grid()
        # state["state"] = consts.RUNNING_STATE

    pygame.display.flip()