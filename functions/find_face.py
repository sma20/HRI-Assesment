#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:47:23 2019

"""
import time
import asyncio
import cozmo
from cozmo.util import degrees, Pose
from cozmo.util import distance_mm, speed_mmps


def find_face(robot: cozmo.robot.Robot):
    global pose

    print ("cozmo is looking for a human face")


    face = None

    # two cubes spotted, the robot will find the human face and approach it.

    while True:


        if face and face.is_visible:


            robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

            robot.say_text("Hello Human").wait_for_completed()

            robot.go_to_pose(Pose(pose.position.x, pose.position.y, pose.position.z,
                                  angle_z=degrees(pose.rotation.angle_z.degrees)),
                             relative_to_robot=True).wait_for_completed()
            break


        else:
            robot.turn_in_place(degrees(30)).wait_for_completed()

            # Wait until we we can see another face
            try:

                face = robot.world.wait_for_observed_face(timeout=2)
                print(face)
            except asyncio.TimeoutError:
                print("Didn't find a face.")
                # return

        time.sleep(1)
    return