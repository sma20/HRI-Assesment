#!/usr/bin/env python3

import os
import sys
import time
import asyncio
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo import nav_memory_map
from cozmo.util import degrees, Pose
from functions.get_in_position import get_in_position
from functions.explore_the_world import explore_the_world
from functions.find_face import find_face
from functions.ar_marker_detection import cozmo_action_ar_marker_cards, reset_sequence
from functions.action_sequence import *
from functions.cube_stack import *

############################################### Map ##############################################

def cozmo_program(robot: cozmo.robot.Robot):
     reset_sequence()
     pose = robot.pose
     cube, cube1 = explore_the_world(robot)

     get_in_position(robot)

     face = find_face(robot)
     robot.go_to_pose(pose, relative_to_robot=False).wait_for_completed()

     #anim = robot.play_anim_trigger(cozmo.anim.Triggers.AcknowledgeFaceNamed)
     #anim.wait_for_completed()
     #robot.say_text("I will try to stack the cubes first").wait_for_completed()
     #robot.say_text("Then it will be your turn").wait_for_completed()
     #anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited)
     #anim.wait_for_completed()

#demo
     #cube_stack(robot)
     #reset_cube(robot)

# add communication


############################################## Game Preparation ###################################

# reset game
# Victory condition check
# if victory is false -> Reset game
# Explain game rules to the player

############################################# Play the game ######################################

# Show markers
     #robot.say_text("It's your turn now!").wait_for_completed()

     robot.say_text("Show me the cards and i will execute the actions").wait_for_completed()
     robot.say_text("Remember, The goal is to stack the cubes").wait_for_completed()
     result = cozmo_action_ar_marker_cards(robot)
     print(result)

     print("im here")
     execute_sequence(robot, result)

    # add communication
# Store the sequence of the control cards
# Execute the actions.
# Victory condition check

############################################# Game result ########################################

# add communication




cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program, use_viewer=True)
#cozmo.run_program(execute_sequence)
