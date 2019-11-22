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

############################################### Map ##############################################

def cozmo_program(robot: cozmo.robot.Robot):
     reset_sequence()
     cube, cube1 = explore_the_world(robot)

     get_in_position(robot)

     face = find_face(robot)
    


# add communication
    
############################################## Game Preparation ###################################    

# Victory condition check
# if victory is false -> Reset game
# Explain game rules to the player

############################################# Play the game ######################################

# Show markers
     
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
