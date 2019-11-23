#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cozmo

def emot_game_success(robot):
    textSay = "Excellent you won the game"
    robot.say_text(textSay, voice_pitch=1.0, duration_scalar=1.0).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()

