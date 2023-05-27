import os
from tkinter import *     # * used to import all funct in c
from PIL import Image,ImageTk
import pygame



pygame.mixer.init()
player=Tk()
player.title('muscic player')
player.geometry('728x410')
img=Image.open("D:\Wallpapers\wp5475508-anime-scenery-night-4k-wallpapers.jpg")
myimg=ImageTk.PhotoImage(img)
lable=Label(player,image=myimg)
lable.place(x=0,y=0)

playlist=Listbox(player,selectmode=SINGLE,font=("arial",13),bg='Black',fg='White',width=50)
os.chdir(r"C:\Users\ASHOK YADAV\OneDrive\Desktop\songs")
songs=os.listdir()
for i in songs:
    pos=0
    playlist.insert(END,i)
    pos+=3


def play():
    curnt=playlist.get(ACTIVE)
    pygame.mixer.music.load(curnt)
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
def stop():
    pygame.mixer.music.stop()
def volume(vol):
    z=int(vol)/100
    pygame.mixer.music.set_volume(z)






bt=Button(player,text="play",width=5,height=3,command=play)
bt.place(x=1,y=350)
bt=Button(player,text="pause",width=5,height=3,command=pause)
bt.place(x=50,y=350)
bt=Button(player,text="unpause",width=5,height=3,command=unpause)
bt.place(x=100,y=350)
bt=Button(player,text="stop",width=5,height=3,command=stop)
bt.place(x=150,y=350)
playlist.place(x=0,y=0)
scale=Scale(player,from_=0,to=100,orient=VERTICAL,length=170,bg='Black',fg='White',command=volume)
scale.place(x=500,y=200)



player.mainloop()