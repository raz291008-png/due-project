import pygame
import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_soldier():
    soldier = pygame.image.load(consts.SOLDIER_PNG)
    sized = pygame.transform.scale(soldier,(consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))
    sized.blit(sized,(0,0))

def draw_mines():
    pass

def draw_explosion():
    pass

def welcome_msg():
    pass

def draw_flag():
    pass

def draw_game():
    pass

draw_soldier()