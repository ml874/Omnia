import aiml
import os
from VoiceInput import VoiceInput


# GLOBAL VARIABLES
say = 'say '
voiceinput = VoiceInput()

kernel = aiml.Kernel()
# kernel.learn("/Users/maverick/Documents/PycharmProjects/Omnia/AIML Files/std-startup.xml")
# kernel.respond("load aiml b")

if os.path.isfile("/Users/maverick/Documents/PycharmProjects/Omnia/AIML Files/brain.brn"):
    kernel.bootstrap(brainFile="/Users/maverick/Documents/PycharmProjects/Omnia/AIML Files/brain.brn")
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    kernel.saveBrain("/Users/maverick/Documents/PycharmProjects/Omnia/AIML Files/brain.brn")

while True:
    # respond = kernel.respond(str(voiceinput.voiceinput()))
    respond = kernel.respond(raw_input("Type Message: "))
    print respond
    # os.system('say ' + respond)
