# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext = 'Welcome. to. geeksforgeeks. hello. nishanth, how may i help you'

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
file = open("/Users/nishanthkrishna/Desktop/Desktop – MacBook Air/PROJECTS/Python text to voice/27 and 28.txt", "r").read().replace("\n", " ")


myobj = gTTS(text=str(file), lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("27 and 28.mp3") 

# Playing the converted file 
#os.system("mpg321 welcome.mp3") 

