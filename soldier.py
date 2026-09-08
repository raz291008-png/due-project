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
    lst = [soldier.get("x")]
    y = soldier.get("y")
    y = consts.SOLDIER_BODY_ROWS * y
    lst.append(y)
    return lst

# def find_arms(soldier):
#     lst = [soldier.get("x")]

def move_soldier(dr,dc,soldier):
    if soldier.get("row")+ dr > 49 or soldier.get("row")+ dr<0:
        soldier["col"] = soldier.get("col") + dc

    elif soldier.get("col")+dc >24 or soldier.get("col")+dc<0:
        soldier["row"] = soldier.get("row") + dr

    else:
        soldier["row"] = soldier.get("row")+ dr
        soldier["col"] = soldier.get("col")+dc


