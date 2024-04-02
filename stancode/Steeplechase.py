"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre-condition:Karel is on the left side of the wall, facing East
    Post-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def down():
    """
    Pre-condition:Karel is at the upper right, facing South
    Post-condition:facing East
    """
    while front_is_clear():
        move()
    else:
        turn_left()


def cross():
    """
    Pre-condition:Karel is facing North
    Post-condition:Karel is at the upper right, facing South
    """
    turn_right()
    move()
    turn_right()


def up():
     """
     Pre-condition:Karel is on the left side of the wall, facing East
     Post-condition:Karel is facing North
     """
     turn_left()
     #Facing North
     while not right_is_clear():
         move()

     """
       while not front_is_clear():
           turn_left()
           move()
           turn_right()
       """



def turn_right():
     for i in range(3):
         turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
