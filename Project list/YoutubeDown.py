from pytube import YouTube

# youtube video link
link = "https://www.youtube.com/watch?v=4R18S7stN5A"
youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

video = youtube_1.streams.all()
# video = youtube_1.streams.filter(only_audio=True)    -> only audio
vid = list(enumerate(video))
for i in vid:
    print(i)

# striming
strm = int(input("enter : "))

video[strm].download()
print('Successfully')