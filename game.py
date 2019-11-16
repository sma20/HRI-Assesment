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



############################################### Map ##############################################

def cozmo_program(robot: cozmo.robot.Robot):
    explore_the_world(robot)

    get_in_position(robot)

    find_face(robot)
    cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program, use_viewer=True)

# add communication
    
############################################## Game Preparation ###################################    

# Victory condition check
# Reset game
# Explain game rules to the player

############################################# Play the game ######################################

# Show markers
# add communication
# Store the sequence of the control cards
# Execute the actions.
# Victory condition check

############################################# Game result ########################################

# add communication


