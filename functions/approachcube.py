#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:09:22 2019

@author: Mariam
"""


import asyncio

import cozmo
from cozmo.util import degrees, distance_mm


def approach_cube(robot: cozmo.robot.Robot):
    '''The core of the go to object test program'''

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(degrees(0)).wait_for_completed()

    # look around and try to find a cube
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    cube = None

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        print("Found cube: %s" % cube)
    except asyncio.TimeoutError:
        print("Didn't find a cube")
    finally:
        # whether we find it or not, we want to stop the behavior
        look_around.stop()

    if cube:
        robot.say_text("Let's go").wait_for_completed()
        # Drive to 70mm away from the cube (much closer and Cozmo
        # will likely hit the cube) and then stop.
        action = robot.go_to_object(cube, distance_mm(70.0))
        action.wait_for_completed()
        print("Completed action: result = %s" % action)
        print("Done.")


#cozmo.run_program(approach_cube)