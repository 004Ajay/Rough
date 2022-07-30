# Make a Text to Speech Software in python with 
# Output Audio Speed Control & Voice Recognition from user 
# V_Recog -> like Mm.. Yes..

from gtts import gTTS as gt
import os

sen = input("Enter the sentence:\n") # getting text from user for conversion to audio

# text -> pass your sentence
# lang -> your preferred language
# slow -> speed of output audio, pass as true or false
myobj = gt(text = sen, lang = 'en', slow = True)

try:
    # Saving the converted audio in a mp3 file
    myobj.save("new.mp3")
    print("File saved to Desktop")
    # Playing the converted file
    os.system("new.mp3")
except:
    print("Unable to process")