#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:54:49 2019

@author: Mariam
"""

#Detect cube (find a cube in the current camera view)
'''Make Cozmo look around for a cube.

Cozmo looks around, reacts, and picks up and puts down a cube if found.
'''

import asyncio

import cozmo
from cozmo.util import degrees


def detect_cube(robot: cozmo.robot.Robot):
    robot.say_text("Where is the cube?").wait_for_completed()
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    # try to find a block
    cube = None
    

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        print("Found cube", cube)
        robot.say_text("Yes i Found the cube").wait_for_completed()
        cubepose = cube.pose
        print("cube position:", cubepose)
        
    except asyncio.TimeoutError:
        print("Didn't find a cube :-(")
        robot.say_text("Time Out! No cube").wait_for_completed()
    finally:
        # whether we find it or not, we want to stop the behavior
        look_around.stop()

    if cube is None:
        robot.say_text("i cant see any cube").wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail)
        
        return

    print("Yay, found cube")
    robot.say_text("Yes i see the cube").wait_for_completed()

    cube.set_lights(cozmo.lights.green_light.flash())

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.BlockReact)
    anim.wait_for_completed()



#cozmo.run_program(detect_cube)




#cozmo.run_program(go_to_object_test)

#Approach cube (move towards the cube until Cozmo touches it)

#Raise forklift
#Lower forklift
#Turn left (turn 90 deg counter clockwise)
#Turn right (turn 90 clockwise)
#Move forward (move 10cm forward)
#Move backward (move 10cm backward)


#excecution card