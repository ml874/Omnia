# import aiml
import os
from VoiceInput import VoiceInput
import unittest

# GLOBAL VARIABLES
say = 'say '
voiceinput = VoiceInput()


##### UNIT TEST AIML #############
class TestAIML(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()



# kernel = aiml.Kernel()
# # kernel.learn("/Users/maverick/Documents/PycharmProjects/Omnia/AIML Files/std-startup.xml")
# # kernel.respond("load aiml b")

# if os.path.isfile("AIML Files/brain.brn"):
#     kernel.bootstrap(brainFile="AIML Files/brain.brn")
# else:
#     kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
#     kernel.saveBrain("AIML Files/brain.brn")

# while True:
#     # respond = kernel.respond(str(voiceinput.voiceinput()))
#     respond = kernel.respond(raw_input("Type Message: "))
#     print respond
#     # os.system('say ' + respond)
