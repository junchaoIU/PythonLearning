__author__ = "小柒"
__blog__ = "https://blog.52itstyle.vip/"
import time
import random
import os
import pygame

"""
树莓派打造智能闹钟
pip3 install pygame
https://blog.52itstyle.vip/
https://www.pygame.org/contribute.html
"""


def py_game_player(file):
    pygame.mixer.init()
    print("播放音乐")
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=10, start=0.0)
    time.sleep(60*10)
    pygame.mixer.music.stop()


if __name__ == '__main__':
    # Linux设置绝对路径
    # mp3 = "/home/pi/alarmClock/"+str(random.randint(1, 6)) + ".mp3"
    mp3 = str(random.randint(1, 6)) + ".mp3"
    print(mp3)
    py_game_player(mp3)
