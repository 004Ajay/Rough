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