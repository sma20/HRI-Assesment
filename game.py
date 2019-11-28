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
     logging.basicConfig(format='%(asctime)s - %(message)s', filename="cozmo_program.log", level=logging.INFO)
     reset_sequence()
     pose = robot.pose
     
# explore world
     logging.info("Cozmo starts exploring")
     cube, cube1 = explore_the_world(robot)
     logging.info("Cozmo detected Cubes:", cube, cube1)

     get_in_position(robot)

# meet the player
     face = find_face(robot)
     logging.info("Identified Face:", face)
     robot.go_to_pose(pose, relative_to_robot=False).wait_for_completed()

  
############################################## Game Preparation ###################################
     
     robot.say_text("I will try to stack the cubes first").wait_for_completed()
     robot.say_text("Then it will be your turn").wait_for_completed()
   

# Autonomous play
     cube_stack(robot)

     logging.info("Victory Condition check - Cozmo game")
     
# Victory condition check
     if abs(cube.pose.position.z - cube1.pose.position.z) > 40: # Assuming cube height (z) is 40mm.
          logging.info("Cube is successfully stacked")
     else:
          logging.info("Cube stack failed!")
          
# reset game

     reset_game(robot)

############################################# Play the game ######################################

# Explain game rules to the player

     robot.say_text("It's your turn now!").wait_for_completed()

     robot.say_text("You need to show me the cards and i will execute the actions").wait_for_completed()
     robot.say_text("Remember, The goal is to stack the cubes").wait_for_completed()
     victory_flag=1

     logging.info("Human interaction with cozmo starts")
     while (victory_flag):
          reset_sequence()
          
# Show markers
          result = cozmo_action_ar_marker_cards(robot)
          logging.info("Marker Cards detected - Action Sequence results: ", result)

# Execute the actions.
          logging.info("Executing Sequence")
          execute_sequence(robot, result)
          
############################################# Game result ########################################

# results of the game
          
          logging.info("Victory condition check - Human game")
          if abs(cube.pose.position.z - cube1.pose.position.z) > 40:  # Assuming cube height (z) is 40mm.
               logging.info("Cube is successfully stacked")
               robot.say_text("Well done").wait_for_completed()
               victory_flag = 0
          else:
               logging.info("Cube stack failed!")
               logging.info("Reset the game and start again! Press Cntrl + C to exit")
               robot.say_text("Nice try! do you want to play again?").wait_for_completed()
               break


cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program, use_viewer=True)
#cozmo.run_program(execute_sequence)
