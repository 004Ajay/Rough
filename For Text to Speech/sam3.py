# Make a Text to Speech Software in python with 
# Output Audio Speed Control & Voice Recognition from user 
# V_Recog -> like Mm.. Yes..

import imp
from gtts import gTTS # Google Text-to-Speech Library
import os
from tkinter import * # for GUI


root = Tk()
root.geometry("300x300")
root.title("Text to Speech")

lb = Label(text = "Enter your text here:") # heading
inputtxt = Text(root, height = 10, width = 25, bg = "white")
Output = Text(root, height = 3, width = 30, bg = "White") # Output screen

def input():
	inp = inputtxt.get("1.0", "end-1c") # getting text from user for conversion to audio
    sen = inp
	print(sen)
    # text -> pass your sentence
    # lang -> your preferred language
    # slow -> speed of output audio, pass as true or false
toAudio = gTTS(text = sen, lang = 'en', slow = True) # converting text to audio
    
    try:
        toAudio.save("new.mp3")  # Saving the converted audio in a mp3 file
        main =  open("new.mp3", "rb").read() # opening saved mp3 file for copying to another location
        with open('C:/Users/ASUS/Desktop/audio.mp3',  'wb+') as dest: # change path as your need
            dest.write(main)
        print("File saved to Desktop") 
        os.system("new.mp3") # playing the text inside program
        Output.insert(END, 'Working on it')
    except:
        Output.insert(END, "Unable to process")
	


Display = Button(root, height = 2, width = 20, text = "Convert", command = lambda:input())

lb.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()