import pygame
import consts

def create_soldier():
    return {
        "row" : 0,
        "col": 0,
        "x": 0 ,
        "y": 0 ,
    }


def find_legs(soldier):
    lst_legs = []
    r = soldier.get("row")+consts.SOLDIER_BODY_ROWS
    c = soldier.get("col")
    for i in range(2):
        lst_legs.append([r,c])
        c = soldier.get("col") +1
    return lst_legs

def find_body(soldier):
    lst_body = []
    r = soldier.get("row")
    c = soldier.get("col")
    c2 = soldier.get("col")+1
    for i in range (consts.SOLDIER_BODY_ROWS):
        lst_body.append([r,c])
        lst_body.append([r,c2])
        r += 1
    return lst_body




def move_soldier(dr,dc,soldier):
    print(dr,dc)
    if 0 <= soldier["row"]+dr < consts.BOARD_ROWS-consts.SOLDIER_BODY_ROWS and 0 <= soldier["col"]+dc < consts.BOARD_COLS-consts.SOLDIER_FEET_ROWS-1:
        soldier["row"] = soldier["row"] + dr
        soldier["col"] = soldier["col"]+dc
        soldier["x"] = soldier["col"] *20
        soldier["y"] =soldier["row"]*20
        print(soldier)
    else:
        print("didnt move")

