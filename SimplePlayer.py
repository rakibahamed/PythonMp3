import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *


root = Tk()
#root.minsize(600,300)

hlist = []
qlist = []
listofsongs = []
realnames = []
v = StringVar()
songlabel = Label(root,textvariable=v,width=100)


def createListbox():
    for items in realnames:
        listbox.insert(END,items)

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

def updatelabel(ind):
    v.set(realnames[ind])

def prevsong(event):
    pop = hlist.pop()
    pygame.mixer.music.load(listofsongs[pop])
    pygame.mixer.music.play()
    updatelabel(pop)
    hbox.delete(0)


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def playsong(event):
    pygame.mixer.music.load(listofsongs[qlist[0]])
    pygame.mixer.music.play()
    updatelabel(qlist[0])
    dqSong()

def qSelection(self):
    selection = qbox.curselection()
    print(selection)
    print(qlist[selection[0]])
    playsong(qlist[selection[0]])

def dqSong():
    hbox.insert(0, qbox.get(0))
    hlist.append(qlist[0])
    qlist.remove(qlist[0])
    qbox.delete(0)


def qSong(event):
    select = listbox.curselection()
    qlist.append(select[0])
    qbox.insert(END,realnames[select[0]])


def createButtons():
    playbutton = Button(root, text = 'Play')
    playbutton.pack()

    previousbutton = Button(root,text = 'Previous')
    previousbutton.pack()

    stopbutton = Button(root,text='Stop')
    stopbutton.pack()

    qbutton = Button(root, text = 'Queue')
    qbutton.pack()

    listbox.bind("<Double-Button-1>", qSong)
    playbutton.bind("<Button-1>", playsong)
    previousbutton.bind("<Button-1>",prevsong)
    stopbutton.bind("<Button-1>",stopsong)
    qbutton.bind("<Button-1>",qSong)




label = Label(root,text='Music Selection')
label.pack()
listbox = Listbox(root, width = 75)
listbox.pack()

qlabel = Label(root,text='Playlist')
qlabel.pack()
qbox = Listbox(root, width = 75)
qbox.pack()

hlabel = Label(root,text='Music History')
hlabel.pack()
hbox = Listbox(root, width = 75)
hbox.pack()


createListbox()
createButtons()

songlabel.pack()

root.mainloop()
