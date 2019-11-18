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
from functions.ar_marker_detection import cozmo_action_ar_marker_cards



############################################### Map ##############################################

def cozmo_program(robot: cozmo.robot.Robot):
    explore_the_world(robot)

    get_in_position(robot)

    find_face(robot)
    cozmo.robot.Robot.drive_off_charger_on_connect = False


# add communication
    
############################################## Game Preparation ###################################    

# Victory condition check
# if victory is false -> Reset game
# Explain game rules to the player

############################################# Play the game ######################################

# Show markers
    cozmo_action_ar_marker_cards(robot)
# add communication
# Store the sequence of the control cards
# Execute the actions.
# Victory condition check

############################################# Game result ########################################

# add communication
    
    
    
    
    
cozmo.run_program(cozmo_program, use_viewer=True)

