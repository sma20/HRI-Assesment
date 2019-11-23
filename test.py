#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:16:33 2019

@author: Mariam
"""
#turn left
import cozmo
import time
import asyncio
from cozmo.util import degrees, distance_mm, speed_mmps
from functions.detectcube import detect_cube
from functions.approachcube import approach_cube
from functions.raiseforklift import cozmo_lift_up
from functions.lowerforklift import cozmo_lift_down
from functions.turnleft import turn_left
from functions.turnright import turn_right
from functions.driveforward import drive_forward
from functions.movebackward import move_backward

global robot


def test(robot):
    
     robot.say_text("CodeLabHappy").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy)
     anim.wait_for_completed()
    
     robot.say_text("CodeLabExcited").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited)
     anim.wait_for_completed()
     
     robot.say_text("CodeLabDancingMambo").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDancingMambo)
     anim.wait_for_completed()
    
     robot.say_text("CodeLabCelebrate").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabCelebrate)
     anim.wait_for_completed()
     
     robot.say_text("AcknowledgeFaceNamed").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.AcknowledgeFaceNamed)
     anim.wait_for_completed()
     
     
     robot.say_text("BlockReact").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.BlockReact)
     anim.wait_for_completed()
     
     robot.say_text("CodeLab123Go").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLab123Go)
     anim.wait_for_completed()
     
     robot.say_text("CodeLabAmazed").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabAmazed)
     anim.wait_for_completed()
     
     
     robot.say_text("AcknowledgeObject").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.AcknowledgeObject)
     anim.wait_for_completed()
     
     robot.say_text("AskToBeRightedLeft").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedLeft)
     anim.wait_for_completed()
     
     robot.say_text("AskToBeRightedRight").wait_for_completed()
     anim = robot.play_anim_trigger(cozmo.anim.Triggers.AskToBeRightedRight)
     anim.wait_for_completed()
     
     
     

cozmo.run_program(test)
