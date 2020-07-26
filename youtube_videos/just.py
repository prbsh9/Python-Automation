from pytube import YouTube

vidUrl = 'https://www.youtube.com/watch?v=1zacYmrdexA'
# video = print(YouTube(vidUrl).streams.order_by('resolution')[-2].download())
audio = YouTube(vidUrl).streams.filter(only_audio=True)[0].download()


