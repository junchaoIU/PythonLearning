# -*- coding: utf-8-*-
__author__ = "小柒"
__blog__ = "https://blog.52itstyle.vip/"
import pyttsx3
import win32com.client
"""
pip3 install pypiwin32
pip3 install pyttsx3
https://blog.52itstyle.vip/
https://pyttsx3.readthedocs.io/en/latest/
"""


def say():
    engine = pyttsx3.init()
    # 音色
    voices = engine.getProperty('voices')
    # 语速
    rate = engine.getProperty('rate')
    # 音量
    volume = engine.getProperty('volume')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.setProperty('rate', rate + 50)
        engine.setProperty('volume', volume + 1.9)
        engine.say("小柒2012真帅")
    engine.runAndWait()


def win_say():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("你好，小姐姐，能加个微信吗？")


def txt():
    f = open("52itstyle.txt", encoding='UTF-8')
    line = f.readline()
    engine = pyttsx3.init()
    while line:
        line = f.readline()
        print(line, end='')
        engine.say(line)
    engine.runAndWait()
    f.close()


if __name__ == '__main__':
    win_say()
    # txt()



