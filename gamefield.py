import random
import consts

game_field =[]
def random_mine ():
    for row in range(20):
        r = random.randint(0,consts.BOARD_ROWS-1)
        c = random.randint(0,consts.BOARD_COLS-1)
        place_mine(r,c)

def place_mine(r,c):
    if c == 0:
        for i in range(3):
            game_field[r][i]=consts.MINE_TILE

    elif c == 49:
        for i in range(47,50):
            game_field[r][i] = consts.MINE_TILE

    else:
        for i in range(c-1,c+2):
            game_field[r][i] = consts.MINE_TILE





def create():
    global game_field
    for r in range(consts.BOARD_ROWS):
        game_field.append([])
        for c in range(consts.BOARD_COLS):
            game_field[r].append(0)


def update():
    pass

def place_flag():
    for r in range(22,25):
        for c in range(46,50):
            game_field[r][c] = consts.FLAG_TILE

