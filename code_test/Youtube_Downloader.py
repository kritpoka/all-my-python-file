from pytube import YouTube
from tkinter import *
"""link = input("enter ur youtube url : ")
yt = YouTube(link)
videos = yt.streams.all()

video =list(enumerate(videos))

for i in video:
    print(i)

print("enter the disired option to download the format")
dn_option = int(input("enter the option : "))
dn_video = videos[dn_option]
dn_video.download()

print("downloaded succesfullly")"""

def download():
    link = get_url.get()
    yt = YouTube(link)
    videos = yt.streams.all()
    strings = str("")

    video =list(enumerate(videos))

    for i in video:
        i = str(i)
        strings += i + '\n'

    var.set(strings)
    infooption.config(text="enter the disired option to download the format")
    infooption.pack()
    choose.pack()
    choosed.pack()

    dn_option = int(input("enter the disired option to download the format"))
    dn_option = int(dn_option)
    dn_video = videos[dn_option]
    dn_video.download()
    infooption.config(text="downloaded succesfully")

root = Tk()
root.title("Youtube Downloader")
root.minsize(width=500, height=400)

var = StringVar()
time_wait = IntVar()

text = Label(root, text="Enter ur youtube url")
text.pack()

get_url = Entry(root)
get_url.pack()

btn = Button(root, text="Enter", command=download)
btn.pack()

info = Label(root, textvariable=var,).pack()

infooption = Label(root)

choose = Entry(root)

choosed = Button(root, text="Enter", command=lambda: time_wait.set(10))

root.mainloop()