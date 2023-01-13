from pytube import YouTube

link = input("enter ur youtube url : ")
yt = YouTube(link)
videos = yt.streams.all()

video =list(enumerate(videos))

for i in video:
    print(i)

print("enter the disired option to download the format")
dn_option = int(input("enter the option : "))
dn_video = videos[dn_option]
dn_video.download()

print("downloaded succesfullly")
