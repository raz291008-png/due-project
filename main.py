import pygame
import consts
import random
import gamefield
import soldier
import screen

state = {
    "is_window_open" : True,
    "soldier" : None,
    "state" : consts.RUNNING_STATE
}
def main():
    pygame.init()
    gamefield.create()

    while state["is_window_open"]:

        handle_user_events()

        if touched_flag():
            state["state"] = consts.WIN_STATE

        elif touched_mine():
            state["state"] = consts.LOSE_STATE

        gamefield.update()
        screen.draw_game()







def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

def touched_flag():
    return True

def touched_mine():
    return True