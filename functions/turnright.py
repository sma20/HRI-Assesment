#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:16:33 2019

@author: Mariam
"""
#turn left
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def turn_right(robot: cozmo.robot.Robot):
    
    # Turn 90 degrees to the right.
    robot.turn_in_place(degrees(-90)).wait_for_completed()


#cozmo.run_program(turn_right)