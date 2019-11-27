#!/usr/bin/env python3

import os
import sys
import time
import asyncio
import logging
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
from functions.resetgame import *


############################################### Map ##############################################

def cozmo_program(robot: cozmo.robot.Robot):
     logging.basicConfig(filename="cozmo_program.log", level=logging.INFO)
     reset_sequence()
     pose = robot.pose
     cube, cube1 = explore_the_world(robot)
     logging.info("Cozmo detected Cubes:", cube, cube1)

     get_in_position(robot)

     face = find_face(robot)
     logging.info("Identified Face:", face)
     robot.go_to_pose(pose, relative_to_robot=False).wait_for_completed()

     #anim = robot.play_anim_trigger(cozmo.anim.Triggers.AcknowledgeFaceNamed)
     #anim.wait_for_completed()

     robot.say_text("I will try to stack the cubes first").wait_for_completed()
     robot.say_text("Then it will be your turn").wait_for_completed()
     #anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited)
     #anim.wait_for_completed()

#demo
     cube_stack(robot)

     logging.info("Victory Condition check - Cozmo game c position",cube.pose.position, "c1 pos", cube1.pose.position)
     #if abs(cube.pose.position.z - cube1.pose.position.z) > 40: # Assuming cube height (z) is 40mm.
          #logging.info("Cube is successfully stacked")
     #else:
          #logging.info("Cube stack failed!")
          #reset_game(robot)
# add communication


############################################## Game Preparation ###################################

# reset game
# Victory condition check
# if victory is false -> Reset game
# Explain game rules to the player

############################################# Play the game ######################################

# Show markers
     robot.say_text("It's your turn now!").wait_for_completed()

     robot.say_text("You need to show me the cards and i will execute the actions").wait_for_completed()
     robot.say_text("Remember, The goal is to stack the cubes").wait_for_completed()
     victory_flag=1

     logging.info("Human interaction with cozmo starts")
     #while (victory_flag):
     #reset_sequence()

     result = cozmo_action_ar_marker_cards(robot)
     logging.info("Marker Cards detected - Action Sequence results: ", result)


     logging.info("Executing Sequence")
     execute_sequence(robot, result)

     logging.info("Victory condition check - Human game c position",cube.pose.position, "c1 pos", cube1.pose.position)
          #if abs(cube.pose.position.z - cube1.pose.position.z) > 40:  # Assuming cube height (z) is 40mm.
               #logging.info("Cube is successfully stacked")
               #victory_flag = 0
          #else:
               #logging.info("Cube stack failed!")
               #logging.info("Reset the game and start again! Press Cntrl + C to exit")

# add communication
# Store the sequence of the control cards
# Execute the actions.
#


############################################# Game result ########################################

# add communication




cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program, use_viewer=True)
#cozmo.run_program(execute_sequence)
