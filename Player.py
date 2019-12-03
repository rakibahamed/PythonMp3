import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3



root = Tk()

root.minsize(300,300)

listofsongs = []

index  = 0


def nextSong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def prevSong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def stopSong(event):
    pygame.mixer.music.stop()

def directoryChooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    #pygame.mixer.music.stop()

lable = Label(root, text = "Music Player")
lable.pack()

listbox = Listbox(root)
listbox.pack()

listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)

listofsongs.reverse()

nextbutton = Button(root, text = 'Next Song')
nextbutton.pack()

prevButton = Button(root, text = 'Previous Song')
prevButton.pack()

stopButton = Button(root, text = 'Stop Button')
stopButton.pack()


nextbutton.bind("<Button-1>", nextSong)
prevButton.bind("<Button-1>", prevSong)
stopButton.bind("<Button-1>", stopSong)



directoryChooser()


root.mainloop()


