#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cozmo

def emot_game_success(robot):
    textSay = "Excellent you won the game"
    robot.say_text(textSay, voice_pitch=1.0, duration_scalar=1.0).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()

def emot_game_failure(robot):
    textSay = "Sorry you lost the game."
    robot.say_text(textSay, voice_pitch=2.0, duration_scalar=0.8).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBored).wait_for_completed()
    head_action = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    head_action.wait_for_completed()
    textSay = "No worries Try again"
    robot.say_text(textSay, voice_pitch=2.0, duration_scalar=0.8).wait_for_completed()





cozmo.run_program(emot_game_success, use_viewer=False)
