import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import webbrowser
import time


def myWatchList():
    with open('anime_watch.txt') as aFile:
        iWatch = aFile.read()
    iWatch = iWatch.split('\n')[1:-1]
    return iWatch


def getAnimeInfo():
    htmlanime1 = requests.get("https://www.animefreak.tv/home/latest-episodes", headers={"Accept-Language": "en-US"}).text
    htmlanime2 = requests.get("https://www.animefreak.tv/home/latest-episodes/page/2", headers={"Accept-Language": "en-US"}).text

    animeSoup1 = BeautifulSoup(htmlanime1, 'lxml')
    animeSoup2 = BeautifulSoup(htmlanime2, 'lxml')

    allAnimes1 = animeSoup1.find_all('div', class_="dl-item")
    allAnimes2 = animeSoup2.find_all('div', class_="dl-item")

    iWatch = myWatchList()
    for anime in iWatch:
        anime = anime.split(',')
        animeMy = anime[0]
        episodeMy = int(anime[1])

        def openAnime():
            toadd = animeName + "," + str(episodeNo)
            webbrowser.open(link, new=2)
            with open('anime_watch.txt', 'r') as file:
                lis = file.readlines()

            with open('anime_watch.txt', 'w') as file:
                for line in lis:
                    if animeMy not in line:
                        file.write(line)
                file.write( toadd + '\n')

        for anime in allAnimes1:
            nameAndEpisode = anime.a.text
            animeName = nameAndEpisode.split('                 ')[0].split('-')[0]
            episode = nameAndEpisode.split('                 ')[2].split('\n')[0]
            episodeNo = int(episode.split(" ")[-1])
            timeAgo = anime.find('div', class_='time').text
            link = anime.a.get('href')

            if (animeMy in animeName) and (episodeNo > episodeMy):
                notify = ToastNotifier()
                notify.show_toast(f'{animeName} unseen episode.', link, callback_on_click=openAnime)

                # print(animeName, episode, timeAgo, link)
                print()

        for anime in allAnimes2:
            nameAndEpisode = anime.a.text
            animeName = nameAndEpisode.split('                 ')[0].split('-')[0]
            episode = nameAndEpisode.split('                 ')[2].split('\n')[0]
            episodeNo = int(episode.split(" ")[-1])
            timeAgo = anime.find('div', class_='time').text
            link = anime.a.get('href')
            if (animeMy in animeName) & (episodeNo > episodeMy):

                notify = ToastNotifier()

                notify.show_toast(f'{animeName} unseen episode.', 'Click here to watch it!', callback_on_click=openAnime, duration=10)


            # print(animeName, episodeNo, timeAgo, link)

if __name__ == '__main__':
    while True:
        getAnimeInfo()
        time.sleep(60*1)

