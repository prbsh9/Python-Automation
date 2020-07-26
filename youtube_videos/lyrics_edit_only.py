from moviepy.editor import *
from bs4 import BeautifulSoup
import requests
from pytube import YouTube



def getVideoOnline():
    # using 7clouds
    url = 'https://www.youtube.com/user/monstafluffmusicTV/videos'
    htmlVids = requests.get(url, headers={"Accept-Language": "en-US"}).text
    vidSoup = BeautifulSoup(htmlVids, 'lxml')

    # print(vidSoup.prettify()[:5000])
    allInfo = vidSoup.find_all('div', class_='yt-lockup-content')[:]
    print(len(allInfo))

    for x in range(10):
        print(x)
        # time_ago = allInfo[x].li.find_next_sibling('li').text
        # author = vidSoup.title.text[2:-11]
        video_title = allInfo[x].a.text
        vid_url = 'https://www.youtube.com' + allInfo[x].a.get('href')
        print(video_title + '\n'  '\n' + vid_url)
        print()


def downloadAndEdit(vidUrl, title):
    video = YouTube(vidUrl).streams.order_by('resolution')[-2].download(filename='video_' + title)
    # print(video)
    audiom = YouTube(vidUrl).streams.filter(only_audio=True)[0].download(filename='audio_' + title)
    # print(audio)
    clip = (VideoFileClip(video).fx(vfx.invert_colors))
    clip.write_videofile(title+'.mp4', fps=25, codec='mpeg4', audio=audiom)


def uploadToYoutube():
    pass

# # .fx( vfx.colorx, 0.5))
# clip.write_videofile('videoAfterEdit11.mp4', fps=25, codec='mpeg4')


# getVideoOnline()
# downloadAndEdit('https://www.youtube.com/watch?v=HhRlpTrkMzg', 'It’s different, Emilee Estoya -Too Good (Lyrics) [7clouds Release]')
downloadAndEdit('https://www.youtube.com/watch?v=TtmAD0ieaSQ', 'Jason Derulo - SAVAGE LOVE (Lyrics) Prod. Jawsh 685')

