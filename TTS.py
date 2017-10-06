import speech_recognition as sr
import os


say = 'say '
r = sr.Recognizer()


def test():
    while True:
        with sr.Microphone() as source:
            print "Say Something!"
            audio = r.listen(source)
        try:
            os.system(say + "Did you say : " + str(r.recognize_google(audio)))
            print "Did you say: " + r.recognize_google(audio)
            return "Did you say: " + r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google could not understand audio")
            return "Google could not understand audio"
        except sr.RequestError as e:
            print("Google error; {0}".format(e))
            return "Google error; {0}".format(e)


def query():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print r.recognize_google(audio)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google could not understand audio")
        return "Google could not understand audio"
    except sr.RequestError as e:
        print("Google error; {0}".format(e))
        return "Google error; {0}".format(e)
