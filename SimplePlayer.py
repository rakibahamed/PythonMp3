import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
from tkinter import filedialog

root = Tk()

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

    fileButton = Button(root, text = 'Sort File')
    fileButton.pack()

    playlistButton = Button(root, text = 'Export Playlist')
    playlistButton.pack()

    listbox.bind("<Double-Button-1>", qSong)
    playbutton.bind("<Button-1>", playsong)
    previousbutton.bind("<Button-1>",prevsong)
    stopbutton.bind("<Button-1>",stopsong)
    qbutton.bind("<Button-1>",qSong)
    fileButton.bind("<Button-1>", inputFile)
    playlistButton.bind("<Button-1>", exportPlaylist)

def inputFile(event):

    root.fileName = filedialog.askopenfilename(filetypes=(("Test File", ".txt"), ("All files","*.*")))

    print(root.fileName)
    root.title(root.fileName)
    text1 = open(root.fileName).read()


    T = Text(root, height=15, width=70)
    T.pack()
    T.insert(END,text1)

    lineList = open(root.fileName).readlines()
    quickSort(lineList)
    f = open("inputFileSort.txt", "w")
    f.writelines(lineList)

def exportPlaylist(event):
    playlist = realnames
    quickSort(playlist)

    with open('Playlist.txt', 'w') as playlistfile:
        playlistfile.writelines("%s\n" % p for p in playlist)


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark





label = Label(root,text='Music Selection')
label.pack()
listbox = Listbox(root, width = 75,height=5)
listbox.pack()

qlabel = Label(root,text='Playlist')
qlabel.pack()
qbox = Listbox(root, width = 75,height=5,)
qbox.pack()

hlabel = Label(root,text='Music History')
hlabel.pack()
hbox = Listbox(root, width = 75,height=5,)
hbox.pack()


createListbox()
createButtons()

songlabel.pack()

root.mainloop()
