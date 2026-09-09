import random
import consts
import soldier
game_field = []

def create(soldier):
    global game_field
    for r in range(consts.BOARD_ROWS):
        game_field.append([])
        for c in range(consts.BOARD_COLS):
            game_field[r].append(0)
    place_soldier(soldier)
    random_mines()
    place_flag()

def random_mines():
    for row in range(20):
        r = random.randint(0,consts.BOARD_ROWS-1)
        c = random.randint(0,consts.BOARD_COLS-1)
        while game_field[r][c] != consts.EMPTY_TILE:
            r = random.randint(0, consts.BOARD_ROWS - 1)
            c = random.randint(0, consts.BOARD_COLS - 1)
        place_mine(r, c)

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

def place_flag():
    for r in range(consts.flag_row,consts.BOARD_ROWS):
        for c in range(consts.flag_col,consts.BOARD_COLS):
            game_field[r][c] = consts.FLAG_TILE


def place_soldier(soldier):
    for r in range(soldier["row"],consts.SOLDIER_ROWS):
        for c in range(soldier["col"],consts.SOLDIER_COLS):
            game_field[r][c] = consts.PLAYER_TILE

def update():
    game_field.append(place_soldier(soldier))
    print(game_field)




