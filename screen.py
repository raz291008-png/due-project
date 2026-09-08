import pygame
import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_soldier(soldier):
    soldier_img = pygame.image.load(consts.SOLDIER_PNG)
    sized = pygame.transform.scale(soldier_img,(consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))

    soldier_box = pygame.Surface((consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT),)
    soldier_box.fill(consts.BACKGROUND_COLOR)
    soldier_box.blit(sized,(soldier["x"],soldier["y"]))
    return soldier_box

def draw_mines():
    pass

def draw_explosion():
    pass

def welcome_msg():
    pass

def draw_flag():
    pass

def draw_game(state):
    pass
