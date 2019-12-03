import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.minsize(600,300)


listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=100)

index = 0

listbox = Listbox(root)

def create_listbox():
    for i in range(0, len(listofsongs)):
        listbox.insert(i, listofsongs[i])
    listbox.pack()

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    create_listbox()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])



def nextsong(event):
    global index
    index += 1
    if index >= (len(listofsongs)-1):
        index = 0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    if index < 0:
        index = len(listofsongs)-1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def playsong(event):
    global index
    index = event
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


label = Label(root,text='Music Player')
label.pack()

playbutton = Button(root, text = 'Play')
playbutton.pack()

nextbutton = Button(root,text = 'Next')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous')
previousbutton.pack()

stopbutton = Button(root,text='Stop')
stopbutton.pack()

deleteButton = Button(root, text='Delete',command=lambda listbox=listbox: listbox.delete(ANCHOR))

deleteButton.pack()

def fileSelection(self):
    selection = listbox.curselection()
    print(selection[0])
    playsong(selection[0])



listbox.bind("<Double-Button-1>", fileSelection)
playbutton.bind("<Button-1>",fileSelection)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()
