import os
import speech_recognition as sr


# Call this class whenever you need a voice input
say = 'say '


class VoiceInput:
    def voiceinput(self, audio=True):
        r = sr.Recognizer()
        while True:
            if audio:
                with sr.Microphone() as source:
                    os.system(say + 'Listening')
                    audio = r.listen(source)
                try:
                    # os.system(say + "Did you say : " + str(r.recognize_google(audio)))
                    # print("Did you say: " + r.recognize_google(audio))
                    # audio = str(r.recognize_google(audio))
                    return str(r.recognize_google(audio))
                except sr.UnknownValueError:
                    os.system(say + "Sorry, I could not understand. Please try again.")

                    return ""
                except sr.RequestError as e:
                    os.system("Sorry, the following error occurred; {0}".format(e))
                    return ""
            else:
                with sr.Microphone() as source:
                    print('Listening')
                    audio = r.listen(source)
                try:
                    # os.system(say + "Did you say : " + str(r.recognize_google(audio)))
                    # print("Did you say: " + r.recognize_google(audio))
                    # audio = str(r.recognize_google(audio))
                    return str(r.recognize_google(audio))
                except sr.UnknownValueError:
                    print("Sorry, I could not understand. Please try again.")
                    return ""
                except sr.RequestError as e:
                    print("Sorry, the following error occurred; {0}".format(e))
                    return ""




