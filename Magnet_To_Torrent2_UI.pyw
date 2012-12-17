#!/usr/bin/python
'''
Created on 08 Sep, 2012
@author: makiftasova (makiftasova@gmail.com)

    GNU GENERAL PUBLIC LICENSE - Version 3
                       
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    http://www.gnu.org/licenses/gpl-3.0.txt

'''

### NOTICE: This GUI uses some functions from Magnet_To_Torrent2.py file
###   which created on Apr 19, 2012 by dan and Faless

from Tkinter import *
from tkMessageBox import *
from Magnet_To_Torrent2 import *



class MainWindow(object):
	
	# Defining CONSTANTS until further notice
	global ENTRY_WIDTH
	global WINDOW_X
	global WINDOW_Y
	global X_OFFSET
	global Y_OFFSET
	global RESIZE_X
	global RESIZE_Y
	
	# Defining of ordinary variables begins
	global magnet
	global outputName
	# Defining of ordinary variables ends
	
	
	# This function defines value of CONSTANTS	
	def CONSTANTS(self):
		#Window's geometry variables
		self.ENTRY_WIDTH = 400
		self.WINDOW_X = 500
		self.WINDOW_Y = 295
		self.X_OFFSET = 200
		self.Y_OFFSET = 200
		
		# Resizable window flags 
		# make them FALSE to get cannot resizeable window
		# make them TRUE to get resizable window
		# default: RESIZE_X=TRUE, RESIZE_Y=FALSE
		self.RESIZE_X = TRUE
		self.RESIZE_Y = FALSE
		return
	
	# Functions begins
	
	def __init__(self):
		self.CONSTANTS()
		window.geometry(self.WINDOWS_GEOMETRY())
		window.resizable(width=self.RESIZE_X, height=self.RESIZE_Y) 
		self.MainTitle()
		self.getMagnetLink()
		self.getTorrentName()
		self.convertButton()
		self.exitButton()
		return
		
		
		
	def MainTitle(self):
		self.mainTitle = window.title("Magnet To Torrent 2")	
		return	
		
	def getLink(self):
		self.magnet = self.magnetEntry.get()
		print self.magnet
		return
	
	def getName(self):
		self.outputName = self.torrentEntry.get()
		print self.outputName
		return
	
	def getMagnetLink(self):
		frame = Frame()
		frame.pack(padx=2, pady=2)
		magnetLinkLabel = Label(text="Enter Magnet Link Here:")
		magnetLinkLabel.pack()
		
		frame = Frame()
		frame.pack(padx=2, pady=2)
		
		self.magnetEntry = Entry(width=self.ENTRY_WIDTH)
		self.magnetEntry.pack()
		
		frame = Frame()
		frame.pack(padx=2, pady=2)
		
		button = Button(text="Get Link", command=self.getLink)
		button.pack(anchor=E, padx=5)
		
		frame = Frame()
		frame.pack(padx=20, pady=20)
		return
		
		
	def getTorrentName(self):
		torrentName = Label(text="Enter Torrent Name Here:")
		torrentName.pack()
		
		frame = Frame()
		frame.pack(padx=2, pady=2)
		
		self.torrentEntry = Entry(width=self.ENTRY_WIDTH)
		self.torrentEntry.pack()
		
		frame = Frame()
		frame.pack(padx=2, pady=2)
		
		button = Button(text="Get Name", command=self.getName)
		button.pack(anchor=E, padx=5)
		
		frame = Frame()
		frame.pack(padx=20, pady=20)
		return
	
	def callWorkerFunction(self):
				
		self.outputName = self.outputName+".torrent"
		magnet2torrent(self.magnet, self.outputName)
		showinfo("Convert Successful", 
		detail = "Converting magnet link to .torrent file \
		Successfuly completed")
		return
	
	def printMessage(self, messageString=" "):
		label = Label(text=messageString)
		label.pack(padx=2, pady=2)
				
		
	def convertButton(self):
		button = Button(text="Convert To Torrent", \
				command=self.callWorkerFunction)
		button.pack(side=LEFT, padx=5, pady=5)
		return
	
	def exitButton(self):
		button = Button(text="Quit", command=exit)
		button.pack(side=RIGHT, padx=5, pady=5)
		return
		

# This function prepares geometry() tool's format string		
	def WINDOWS_GEOMETRY(self):
		string = str(self.WINDOW_X)+"x"+str(self.WINDOW_Y)
		string += "+"+str(self.X_OFFSET)+"+"+str(self.Y_OFFSET)
		return string
		

		

if __name__ == "__main__":
	window = Tk()
	MW = MainWindow()
	mainloop()
	
