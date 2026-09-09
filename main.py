import pygame
import consts
import random
import gamefield
import soldier
import screen
from gamefield import game_field

state = {
    "is_window_open" : True,
    "soldier" : None,
    "state" : consts.RUNNING_STATE

}

def main():
    pygame.init()
    state["soldier"] = soldier.create_soldier()
    gamefield.create(state["soldier"])

    while state["is_window_open"]:

        handle_user_events()

        if touched_flag():
            state["state"] = consts.WIN_STATE

        elif touched_mine():
            state["state"] = consts.LOSE_STATE

        gamefield.place_soldier(state["soldier"])
        screen.draw_game(state)



def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j],end= "")
        print("")
    print("\n")



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
            elif event.key == pygame.K_UP:
                dr = -1
            elif event.key == pygame.K_DOWN:
                dr = 1
            elif event.key == pygame.K_LEFT:
                dc = -1
            elif event.key == pygame.K_RIGHT:
                dc = 1
            soldier.move_soldier(dr,dc,state["soldier"])





def touched_flag():
    body = soldier.find_body(state["soldier"])
    for cell in range(len(body)):
        if game_field[body[cell][0]][body[cell][1]] == consts.FLAG_TILE:
            return True
    return False

def touched_mine():
    legs = soldier.find_legs(state["soldier"])
    for cell in range(len(legs)):
        if game_field[legs[cell][0]][legs[cell][1]] == consts.MINE_TILE:
            return True
    return False


if __name__ == '__main__':
    main()