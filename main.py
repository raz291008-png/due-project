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
    print_mat(gamefield.game_field)
    state["soldier"] = soldier.create_soldier()
    while state["is_window_open"]:

        handle_user_events()

        if touched_flag():
            state["state"] = consts.WIN_STATE

        elif touched_mine():
            state["state"] = consts.LOSE_STATE

        gamefield.update()
        screen.draw_game(state)



def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j],end= "")
        print("")



def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            dr, dc = 0, 0
            if event.key == pygame.K_SPACE:
                state["state"] = consts.SHOW_MINES_STATE
                print("ok")
            elif event.key == pygame.K_UP:
                dr = -1
            elif event.key == pygame.K_DOWN:
                dr = 1
            elif event.key == pygame.K_LEFT:
                dc = -1
            elif event.key == pygame.K_RIGHT:
                dc = 1






def touched_flag():
    return True

def touched_mine():
    return True

if __name__ == '__main__':
    main()