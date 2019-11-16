import cozmo

from game import pose

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    #1- check cube1 if its in the initial place do 3 if not do 2
    #2- pickup cube 1 
    #3- go to cube 1 initial position
    #4- PlaceObjectOnGroundHere cube1 
    #5- check cube2
    #7- pickup cube2 
    #8- go to cube2 initial position
    #9- PlaceObjectOnGroundHere cube2 
    #10- go to cozmo initial position
    
    
    robot.go_to_pose(pose(0.0, 0.0, 0.0),relative_to_robot=True).wait_for_completed()
    # cozmo.robot.PickupObject(obj, use_pre_dock_pose=True, **kw)
    # cozmo.robot.PlaceObjectOnGroundHere(obj, **kw)
    
    
    #robot.go_to_pose(pose(pose.position.x, pose.position.y, pose.position.z,
                                 # angle_z=degrees(pose.rotation.angle_z.degrees)),
                            # relative_to_robot=True).wait_for_completed()


cozmo.run_program(cozmo_program)