import os
import speech_recognition as sr


# Call this class whenever you need a voice input
say = 'say '


class VoiceInput:
    def voiceinput(self):
        r = sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                # print "Did you say: " + r.recognize_google(audio)
                audio = str(r.recognize_google(audio))
                return audio
            except sr.UnknownValueError:
                # print("Google could not understand audio")

                return ""
            except sr.RequestError as e:
                # print("Google error; {0}".format(e))
                # pass return "Google error; {0}".format(e)
                return ""
