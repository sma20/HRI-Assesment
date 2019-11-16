#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:19:58 2019

@author: Mariam
"""

# Move backward
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def move_backward(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(-100), speed_mmps(50)).wait_for_completed()


#cozmo.run_program(move_backward)