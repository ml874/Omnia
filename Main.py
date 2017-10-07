import os, pyaudio
import BasicFunctions
import sys
import TTS
import Omnia


# Provide Headlines
def news():
    topnews = say + "Here are some top news headlines for the day"
    os.system(topnews)
    topnews = TopNews.main()
    for headline in topnews:
        try:
            headline = str(headline)
            head, sep, tail = headline.partition(' https')
            os.system(say + head)
        except:
            pass


def askQuestion():
    question = TTS.query()
    Omnia.query(question)

# Provide Requests


if __name__ == '__main__':
    basic = BasicFunctions.Basic()
    basic.goodMorning()
    basic.getweather('Ithaca, New York')
    # news()
    # while True:
    #     askQuestion()
