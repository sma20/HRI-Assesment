#!/usr/bin/env python3
"""
Created on Nov 20, 2019
@author: Arthidevi Balavignesh
"""
import cozmo
import time
import asyncio
from cozmo.util import degrees, distance_mm, speed_mmps
from functions.detectcube import detect_cube
from functions.approachcube import approach_cube
from functions.raiseforklift import cozmo_lift_up
from functions.lowerforklift import cozmo_lift_down
from functions.turnleft import turn_left
from functions.turnright import turn_right
from functions.driveforward import drive_forward
from functions.movebackward import move_backward

global robot
global action_sequence


def execute_sequence(robot, action_sequence):
    
    print(action_sequence)
    for action in range(len(action_sequence)):
        print (action)
        if (action_sequence[action] == 1):
            detect_cube(robot)
        elif (action_sequence[action] == 2):
            approach_cube(robot)
        elif (action_sequence[action] == 3):
            cozmo_lift_up(robot)
        elif (action_sequence[action] == 4):
            cozmo_lift_down(robot)
        elif (action_sequence[action] == 5):
            turn_left(robot)
        elif (action_sequence[action] == 6):
            turn_right(robot)
        elif (action_sequence[action] == 7):
            drive_forward(robot)
        elif (action_sequence[action] == 8):
            move_backward(robot)

