# Basic Functions. Good Morning, Weather, News
import time
import speech_recognition as sr
import os
from weather import Weather
import requests
import loginkeys
from newsapi.articles import Articles
from VoiceInput import VoiceInput


# GLOBAL VARIABLES
say = 'say '
voiceinput = VoiceInput()

class Basic:
    # Good Morning
    def goodMorning(self):
        os.system(say + "Good Morning, Maverick")

    # Local Time
    def localtime(self):
        localtime = time.asctime(time.localtime(time.time()))
        localtime = say + "The time is now " + str(localtime)
        os.system(localtime)

    # Weather
    # def geolocate(self):
    #     req = requests.get('http://freegeoip.net/json/')
    #     location = json.loads(req.text)
    #     req.close()
    #     location_city = location['city']
    #     # location_state = location['region_name']
    #     # location_country = location['country_name']
    #     # location_zip = location['zip_code']
    #     return location
    # Return Weather
    def getweather(self, location):
        weather = Weather()
        data = weather.lookup_by_location(location)
        condition = data.condition()
        cond = condition['text']
        temp = condition['temp']
        weather = say + " Here is the weather for" + location + ". It is " + cond + " with a temperature of " + \
                  temp + " degrees."
        os.system(weather)

    # Return News By Category
    def topnews(self):

        while True:
            os.system(say + 'What news would you like today?')
            sourcenews = voiceinput.voiceinput()
            os.system(say + "Pulling up news from : " + sourcenews)
            sourcenews = '-'.join(sourcenews.split())
            a = Articles(API_KEY=loginkeys.NEWSAPI_KEY)
            try:
                x = a.get(source=sourcenews)
                articles = x['articles']
                descriptions = []

                for x in articles:
                    descriptions.append(str(x['description']))

                    # descriptions.append(x['description'].replace(u"\u2018", "'").replace(u"\u2019", "'"))
                os.system(say + "Here are some top news headlines:")
                os.system(say + str(descriptions))
                break
            except:
                os.system(say + 'Sorry, server was not responding or you said an invalid choice. Please try again.')
                continue


