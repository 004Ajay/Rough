from gtts import gTTS # Google Text-to-Speech Library
import os

sen = input("Enter the sentence:\n") # getting text from user for conversion to audio
# text -> pass your sentence
# lang -> your preferred language
# slow -> speed of output audio, pass as true or false
toAudio = gTTS(text = sen, lang = 'en', slow = True) # converting text to audio

toAudio.save("new.mp3")  # Saving the converted audio in a mp3 file
os.system("sen.mp3") # playing the text inside program