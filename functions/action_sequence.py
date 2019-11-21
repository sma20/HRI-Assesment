#!/usr/bin/env python3
"""
Created on Nov 20, 2019
@author: Arthidevi Balavignesh
"""
from functions.detectcube import detect_cube
from functions.approachcube import approach_cube
from functions.raiseforklift import cozmo_lift_up
from functions.lowerforklift import cozmo_lift_down
from functions.turnleft import turn_left
from functions.turnright import turn_right
from functions.driveforward import drive_forward
from functions.movebackward import move_backward
from functions.cozmo_actions import *

action_sequence = []
ready_flag = 1
global robot1

def add_actions(actionName):
    if (ready_flag):
        action_sequence.append(actionName)
        confirm_card(actionName)
        unset_ready_flag()

def reset_sequence():
    action_sequence = []

def unset_ready_flag():
    ready_flag = 0;

def set_ready_flag():
    ready_flag = 1;

def set_robot_for_action(robot):
    global robot1
    robot1 = robot

#say card name
def confirm_card(cardName):
    global robot1
    switcher = {
        0: "DETECT CUBE",
        1: "APPROACH CUBE",
        2: "RAISE FORK LIFT",
        3: "LOWER FORK LIFT",
        4: "TURN LEFT",
        5: "TURN RIGHT",
        6: "MOVE FORWARD",
        7: "MOVE BACKWARD"
    }
    card_name_text = switcher.get(cardName, "Invalid Action Card")
    print (card_name_text)
    robot1.say_text(card_name_text).wait_for_completed()


def execute_sequence(robot):
    for action in action_sequence:
        print (action)
        switcher = {
            0: detect_cube,
            1: approach_cube,
            2: cozmo_lift_up,
            3: cozmo_lift_down,
            4: turn_left,
            5: turn_right,
            6: drive_forward,
            7: move_backward
        }
        func = switcher.get(action, lambda: 'Invalid')
        func(robot)