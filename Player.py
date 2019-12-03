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

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])



def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
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
<<<<<<< HEAD
    #pygame.mixer.music.stop()
    create_listbox()

def create_listbox():
    listbox = Listbox(root)
    for i in range(0, len(listofsongs)):
        listbox.insert(i, listofsongs[i])
    listbox.pack()



lable = Label(root, text = "Music Player")
lable.pack()

=======
    updatelabel()


label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root, width = 75)
listbox.pack()

realnames.reverse()

for items in realnames:
    listbox.insert(0,items)
>>>>>>> 33974d8f54037c695ad783cf1401efa98f6e51c1

realnames.reverse()


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


<<<<<<< HEAD
root.mainloop()
=======

listbox.bind("<Double-Button-1>", fileSelection)
playbutton.bind("<Button-1>",fileSelection)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()
>>>>>>> 33974d8f54037c695ad783cf1401efa98f6e51c1
