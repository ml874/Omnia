import aiml
import os
from VoiceInput import VoiceInput


# GLOBAL VARIABLES
say = 'say '
voiceinput = VoiceInput()

kernel = aiml.Kernel()
# kernel.learn("aiml/std-startup.xml")
# kernel.respond("load aiml b")

# print(kernel)

if os.path.isfile("aiml/brain.brn"):
    kernel.bootstrap(brainFile="aiml/brain.brn")
else:
    kernel.bootstrap(learnFiles="aiml/std-startup.xml", commands="load aiml b")
    kernel.saveBrain("aiml/brain.brn")

while True:
	# print(kernel.respond(input("Enter your message >> ")))

	voice_input = str(voiceinput.voiceinput(audio=True))
	response = kernel.respond(voice_input)
	# input_text = input("Type Message: ")
	# response = kernel.respond(input_text)
	print(response)
	os.system('say ' + response)
