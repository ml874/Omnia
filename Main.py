import os, pyaudio
import BasicFunctions
import sys
import TTS
import Omnia

def askQuestion():
    question = TTS.query()
    Omnia.query(question)

# Provide Requests


if __name__ == '__main__':
    basic = BasicFunctions.Basic()
    # basic.goodMorning()
    # basic.localtime()
    # basic.getweather('Ithaca, New York')
    basic.topnews()
    # while True:
    #     askQuestion()
