'''from pytube import YouTube

link="https://youtu.be/EAYlckSaviI"

youtube1=YouTube(link)
print()
print(youtube1.thumbnail_url)

video=youtube1.streams.all()

vid=list(enumerate(video))
for i in vid:
    print(i)
print()
stre=int(input("enter resolution :"))
video[stre].download()
print("Sucessfully")'''

#importing the tinkter library
from email.mime import audio
from select import select
import tkinter
from tkinter import Button, Canvas, Entry, Label, PhotoImage, Tk, filedialog
from turtle import title
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
#functions

#to select the download path
def select_path():
    #allow to select path dir
    path=filedialog.askdirectory()
    path_label.config(text=path)
    pass

#to download video
def download_file():
    #get user path
    get_link=link_field.get()
    #get selected path
    user_path=path_label.cget("text")
    screen.title("Downloading.....")
    #Download Video
    mp4_video=YouTube(get_link).streams.get_highest_resolution().download()
    video_clip=VideoFileClip(mp4_video)
    video_clip.close()
    #move file to destined location
    shutil.move(mp4_video,user_path)
    screen.title("Download Complete! Download another file")
    pass

'''#to download audio
def download_audio():
    #get user path
    get_link=link_field.get()
    #get selected path
    user_path=path_label.cget("text")
    #Download Video
    YouTube(get_link).streams.get_audio_only().download()
    pass'''


screen = Tk()
title = screen.title("YouTube Download")
canvas=Canvas(screen,width=500,height=500)
canvas.pack()

#get the image
logo_image=PhotoImage(file="yt.png")
#now resize image
logo_image=logo_image.subsample(2,2)
#create image canvas
canvas.create_image(250,80,image=logo_image)

#link field
link_field=Entry(screen,width=50)
link_label = Label(screen,text="Enter download link",font=('Arial',15))

#select path for saving file
path_label=Label(screen,text="Select path for download",font=('Arial',15))
select_btn=Button(screen,text="Select",command=select_path)

#add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)


#add widgets 
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_field)

#download btns
download_btn_mp4=Button(screen,text="Download Mp4",command=download_file)
#download_btn_mp3=Button(screen,text="Download Mp3",command=download_audio)

#add to canvas
canvas.create_window(250,390,window=download_btn_mp4)
#canvas.create_window(250,420,window=download_btn_mp3)


screen.mainloop()