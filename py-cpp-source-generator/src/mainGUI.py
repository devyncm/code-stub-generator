import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter.font
import os

from SourceGenerator import SourceGenerator

class MyGUI:

	def browseFiles(myGUI):
		filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File" , filetypes = (("Header files","*.h*"),("All files", "*.*")))
		myGUI.text_box.insert(tkinter.END, filename)
		filename = os.path.normpath(filename)
		path_list = filename.split(os.sep)
		#print(path_list)
		

	def saveToString(myGUI):
		#saves the contents of my_str as aan array of all the header files that have to be processed
		my_string = myGUI.text_box.get("1.0", END)
		my_str = my_string.split()
		print(my_str)
		
		srcgen = SourceGenerator()
		for header in my_str:
			srcgen.generate(header)

	def __init__(myGUI):
		#create main window
		myGUI.gui = tkinter.Tk()
		myGUI.gui.title("Code Stub Generator v1.0")
		myGUI.gui.minsize(width=500,height=350)
		myGUI.gui.geometry("600x400")
		myGUI.gui.resizable(True,False)

		#column configs
		myGUI.gui.columnconfigure(1, minsize = 50)
		myGUI.gui.columnconfigure(2, minsize = 50)
		myGUI.gui.columnconfigure(3, minsize = 50)
		myGUI.gui.columnconfigure(4, minsize = 50)
		myGUI.gui.columnconfigure(5, minsize = 50)
		myGUI.gui.columnconfigure(6, minsize = 50)
		myGUI.gui.columnconfigure(7, minsize = 50)
		myGUI.gui.columnconfigure(8, minsize = 50)
		myGUI.gui.columnconfigure(9, minsize = 50)
		myGUI.gui.columnconfigure(10, minsize = 50)
		
		#create heading labels
		myGUI.heading_label = tkinter.Label(text='Code Stub Generator', font=("Helvetica",16), fg="blue")
		myGUI.heading_label.grid(row=0, column=3)

		#create file explorer
		myGUI.label_file_explorer = tkinter.Button(myGUI.gui, text="File Explorer", width=40, command=myGUI.browseFiles)
		myGUI.label_file_explorer.grid(row=4, column=3, pady=10)

		#textbox label
		myGUI.text_labels = tkinter.Label(myGUI.gui, text='Enter the files you wish to generate stubs for')
		myGUI.text_labels.grid(row=2, column=3)

		#textbox added
		myGUI.text_box = tkinter.Text(myGUI.gui, height=10, width=50)
		myGUI.text_box.grid(row=3, column=3)

		#generate button added
		myGUI.button1 = tkinter.Button(myGUI.gui, text='Generate', width=10, command=myGUI.saveToString) 
		myGUI.button1.grid(row=5,column=3, pady=10)

		#quit button added
		myGUI.button2 = tkinter.Button(myGUI.gui, text='Quit', width=10, command=exit)
		myGUI.button2.grid(row=6,column=3, pady=10)
	
		tkinter.mainloop()
my_gui = MyGUI()
