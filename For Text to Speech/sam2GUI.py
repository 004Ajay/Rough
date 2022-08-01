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

def input():
	inp = inputtxt.get("1.0", "end-1c")
	print(inp)
	if(inp == "120"):
		Output.insert(END, 'Correct')
	else:
		Output.insert(END, "Wrong answer")
	
lb = Label(text = "Enter your text here:") # heading

inputtxt = Text(root, height = 10, width = 25, bg = "light yellow")

Output = Text(root, height = 5, width = 5, bg = "light cyan") # Output screen

Display = Button(root, height = 2, width = 20, text = "Convert", command = lambda:input())

lb.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()



while True:
    sen = input("Enter the sentence:\n") # getting text from user for conversion to audio

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
    except:
        print("Unable to process")
    if input("Again? y/n : ") == 'y' or 'Y': # breaking while loop (line 8) if input is Y or y
        break