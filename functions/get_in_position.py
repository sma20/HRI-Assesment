#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:31:34 2019

"""
import cozmo


def get_in_position(robot: cozmo.robot.Robot):
    print("I am in the get in position method")
    if (robot.lift_height.distance_mm > 45) or (robot.head_angle.degrees < 40):
        with robot.perform_off_charger():
            lift_action = robot.set_lift_height(0.0, in_parallel=True)
            head_action = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE,
                                               in_parallel=True)
            lift_action.wait_for_completed()
            head_action.wait_for_completed()