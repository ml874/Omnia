import os, pyaudio
import time
import TopNews
import Weather
import sys
import TTS
import Omnia

say = 'say '


# Good Morning
def goodMorning():
    os.system(say + "Good Morning, Maverick")


# Provide Time
def localtime():
    localtime = time.asctime(time.localtime(time.time()))
    localtime = say + "The time is now " + str(localtime)
    os.system(localtime)


# Provide Weather
def weather():
    city = Weather.geolocate()['city']
    state = Weather.geolocate()['region_name']
    condition = Weather.getweather(city)['text']
    temp = Weather.getweather(city)['temp']
    weather = say + \
              " Here is the weather for" + city + ", " + state + ". It is " + condition + " with a temperature of " + \
              temp + " degrees."
    os.system(weather)


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
    goodMorning()
    localtime()
    # weather()
    news()
    # while True:
    #     askQuestion()
