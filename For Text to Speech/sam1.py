# Make a Text to Speech Software in python with 
# Output Audio Speed Control & Voice Recognition from user 
# V_Recog -> like Mm.. Yes..

from gtts import gTTS as gt
import os

def saveAudio(Audio):
    save_path = "D:\Temp" # 'C:\Users\ASUS\Desktop'
    name = "new.mp3"
    completeName = os.path(save_path, name)         

    with open(completeName, "w") as file1:
        file1.write(Audio)
    print("File saved to Temp")

sen = input("Enter the sentence:\n") # getting text from user for conversion to audio

# text -> pass your sentence
# lang -> your preferred language
# slow -> speed of output audio, pass as true or false
toAudio = gt(text = sen, lang = 'en', slow = True)

try:
    # Saving the converted audio in a mp3 file
    #toAudio.save("new.mp3")
    saveAudio(toAudio)


    # Playing the converted file
    #os.system("new.mp3")
except:
    print("Unable to process")


