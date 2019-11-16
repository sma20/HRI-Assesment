#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:58:19 2019

"""
#Raise forklift

import cozmo
import time

def cozmo_lift_up(robot: cozmo.robot.Robot):
    '''This is a docstring which says that this function moves Cozmo's lift - Code by Kinvert'''
    robot.move_lift(0.25) #radians per second
    time.sleep(3) #3 seconds
    
    
#cozmo.run_program(cozmo_lift_up)