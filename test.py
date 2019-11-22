#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:16:33 2019

@author: Mariam
"""
#turn left
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

# def turn_left():
#     global robot
#     robot.turn_in_place(degrees(-90)).wait_for_completed()
#
# def turn_right():
#     global robot
#     robot.turn_in_place(degrees(90)).wait_for_completed()
#
# def move_forward():
#     global robot
#     robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()

def test2(robot):
    actionArray = [1,2,2,3,2,1,2,3,2,3,1,2]
    for action in range(len(actionArray)):
        print (action)
        if (actionArray[action] == 1):
            turn_left(robot)
        elif (actionArray[action] == 2):
            turn_right(robot)
        elif (actionArray[action] == 3):
            drive_forward(robot)

def test(robot1):
    global robot
    robot = robot1
    test2(robot1)
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(myTaskGenerator())
   # print("Completed All Tasks")
   # loop.close()

# async def myTaskGenerator():
#     actionArray = [1,2,2,3,2,1,2,3,2,3,1,2]
#     for action in range(len(actionArray)):
#         print (action)
#         if (actionArray[action] == 1):
#             asyncio.ensure_future(turn_left())
#         elif (actionArray[action] == 2):
#             asyncio.ensure_future(turn_right())
#         elif (actionArray[action] == 3):
#             asyncio.ensure_future(move_forward())

cozmo.run_program(test)
