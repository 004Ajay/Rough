# Make a Text to Speech Software in python with 
# Output Audio Speed Control & Voice Recognition from user 
# V_Recog -> like Mm.. Yes..

"""

"""

from gtts import gTTS as gt
import os

from sqlalchemy import true

sen = input("Enter the sentence:\n") # getting text from user for conversion to audio

# text -> pass your sentence
# lang -> your preferred language
# slow -> speed of output audio, pass as true or false
myobj = gt(text = sen, lang = 'en', slow = true)

# Saving the converted audio in a mp3 file
myobj.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")