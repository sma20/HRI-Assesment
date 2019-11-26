

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps, Pose, time


def reset_game(robot: cozmo.robot.Robot):
	
	robot.go_to_pose(Pose(0.0, 0.0, 0.0, angle_z=degrees(0)), relative_to_robot=False).wait_for_completed()

