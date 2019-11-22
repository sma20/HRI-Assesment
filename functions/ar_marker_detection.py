#!/usr/bin/env python3
"""
Created on Nov 17, 2019

@author: Sethu Lekshmy
"""


import time
import asyncio
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes
from functions.detectcube import detect_cube
from functions.approachcube import approach_cube
from functions.raiseforklift import cozmo_lift_up
from functions.lowerforklift import cozmo_lift_down
from functions.turnleft import turn_left
from functions.turnright import turn_right
from functions.driveforward import drive_forward
from functions.movebackward import move_backward
from cozmo.util import degrees, distance_mm, speed_mmps
from functions.cozmo_actions import *
from functions.action_sequence import *

def arm_cards_disappeared_event_handler(evt, **kw):
    set_ready_flag()

global robot1
#global execute
global action_sequence
execute = False
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

def add_sequences(robot1):
    print (action_sequence)
    return action_sequence

# Invoked when Cozmo sees AR Marker Cards.
def arm_cards_appeared_event_handler(evt, **kw):
   global robot1, execute
   if isinstance(evt.obj, CustomObject):
        if evt.obj.object_type == CustomObjectTypes.CustomType01:
            print("Invoke DetectCube function")
            add_actions(DETECT_CUBE)
           # detect_cube(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType02:
            print("Invoke ApproachCube function")
            add_actions(APPROACH_CUBE)
           # approach_cube(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType03:
            print("Invoke Raise Fork Lift function")
            add_actions(RAISE_FORK_LIFT)
           # cozmo_lift_up(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType04:
            print("Invoke Lower Fork Lift function")
            add_actions(LOWER_FORK_LIFT)
            # cozmo_lift_down(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType05:
            print("Invoke Turn Left function")
            add_actions(TURN_LEFT)
            # turn_left(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType06:
            print("Invoke Turn Right function")
            add_actions(TURN_RIGHT)
            # turn_right(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType07:
            print("Invoke Move Forward function")
            add_actions(MOVE_FORWARD)
            # drive_forward(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType08:
            print("Invoke Move Backward function")
            add_actions(MOVE_BACKWARD)
           #  move_backward(robot)
        elif evt.obj.object_type == CustomObjectTypes.CustomType09:
            print("Start Execution")
            execute = True
           # add_sequences(robot1)
            return execute

def cozmo_action_ar_marker_cards(robot: cozmo.robot.Robot):
    global robot1
    robot1 = robot
    set_robot_for_action(robot)
    # Event handlers
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, arm_cards_appeared_event_handler)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, arm_cards_disappeared_event_handler)

    # DetectCube - Circles2 Marker (30mm x 30mm)
    detect_cube_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType01,
                                              CustomObjectMarkers.Circles2,
                                              150, 100,
                                              30, 30, True)
    # ApproachCube - Diamonds2 Marker (30mm x 30mm)
    approach_cube_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType02,
                                              CustomObjectMarkers.Diamonds2,
                                              150, 100,
                                              30, 30, True)

    # Raise Fork Lift - Hexagons2 Marker (30mm x 30mm)
    raise_fork_lift_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType03,
                                              CustomObjectMarkers.Hexagons2,
                                              150, 100,
                                              30, 30, True)

    # Lower Fork Lift - Triangles2 Marker (30mm x 30mm)
    lower_fork_lift_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType04,
                                                         CustomObjectMarkers.Triangles2,
                                                         150, 100,
                                                         30, 30, True)

    # Turn Left - Circles3 Marker (30mm x 30mm)
    turn_left_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType05,
                                                         CustomObjectMarkers.Circles3,
                                                         150, 100,
                                                         30, 30, True)

    # Turn Right - Diamonds3 Marker (30mm x 30mm)
    turn_right_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType06,
                                                   CustomObjectMarkers.Diamonds3,
                                                   150, 100,
                                                   30, 30, True)

    # Move Forward - Hexagons3 Marker (30mm x 30mm)
    move_forward_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType07,
                                                    CustomObjectMarkers.Hexagons3,
                                                    150, 100,
                                                    30, 30, True)

    # Move Backward - Triangles3 Marker (30mm x 30mm)
    move_backward_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType08,
                                                    CustomObjectMarkers.Triangles3,
                                                    150, 100,
                                                    30, 30, True)

    # Start Execution - Hexagons5 Marker (30mm x 30mm)
    start_execution_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType09,
                                                       CustomObjectMarkers.Hexagons5,
                                                       150, 100,
                                                       30, 30, True)


    if((detect_cube_obj is not None) and (approach_cube_obj is not None) and
        (raise_fork_lift_obj is not None) and (lower_fork_lift_obj is not None) and
        (turn_left_obj is not None) and (turn_right_obj is not None) and
        (move_forward_obj is not None) and (move_backward_obj is not None) and
        (start_execution_obj is not None)):
        print("All AR Marker detection objects are defined successfully!")
        
       
   # else:
     #   print("One or more AR Marker detection object definitions failed!")
     #   return

   
    
    print("Press CTRL-C to quit")
    while True:
        
        number_cards_shown = len(action_sequence)
       # print(execute)
        if number_cards_shown == 8 and execute == False:
            
            print("Show me the execution card")
          
        if number_cards_shown == 8 and execute == True:
                
                robot.wait_for_all_actions_completed()
                print("marker detection is finished")
                return action_sequence
                break
        if number_cards_shown < 8:
            print(action_sequence)
            #print(number_cards_shown)
        if number_cards_shown < 8 and execute == True:
            print("No execution yet, first show me 8 cards")
            
    time.sleep(1)


