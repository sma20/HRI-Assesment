#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:37:42 2019

"""
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.util import Pose


def explore_the_world(robot: cozmo.robot.Robot):
    global pose

    #initialise the variables
    cube = None
    cube1 = None

    look_around_2 = None
    look_around_3 = None

    # stores the starting location of the cozmo robot
    pose = robot.pose

    print('Pose: Pos = <%.1f, %.1f, %.1f>' % pose.position.x_y_z)
    print('Pose: Rot quat = <%.1f, %.1f, %.1f, %.1f>' % pose.rotation.q0_q1_q2_q3)
    print('Pose: angle_z = %.1f' % pose.rotation.angle_z.degrees)
    print('Pose: origin_id: %s' % pose.origin_id)

    # look around to find the first cube
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    while True:
        try:
            cube = robot.world.wait_for_observed_light_cube(timeout=10)
            if cube:
                print(cube)
                look_around.stop()
                break
            else:

                robot.go_to_pose(Pose(pose.position.x, pose.position.y, pose.position.z,
                                  angle_z=degrees(pose.rotation.angle_z.degrees)),
                             relative_to_robot=True).wait_for_completed()


                robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        except asyncio.TimeoutError:
            print("Didn't find a cube :-(")
        #finally:
            #look_around.stop()

    print("the type of the cube is ", type(cube.cube_id))

    cube1= cube
    id = cube.cube_id
    robot.turn_in_place(degrees(30)).wait_for_completed()

    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    print(id)
    while True:


        try:
            cube1 = robot.world.wait_for_observed_light_cube(timeout=10)
            if cube1.cube_id != id:
                print(cube1)
            else:
                id = cube1.cube_id
                look_around_2 = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

        except asyncio.TimeoutError:
            print("Didn't find a cube :-(")


        finally:
            look_around_3 = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            #robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

        if id != cube1.cube_id:
            break

    print("the new id is ", id)
    look_around.stop()
    if look_around_2:
        look_around_2.stop()
    if look_around_3:
        look_around_3.stop()

    # set the head position for the cozmo robot
    print("both cubes have been spotted ")

    return