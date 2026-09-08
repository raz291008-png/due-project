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

def move_soldier():
    pass