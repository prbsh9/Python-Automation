import requests
from bs4 import BeautifulSoup
import time


def favYoutubersVid(favourateYoutubers, t=7, a=6):
    vids = []
    ''' Did any of your favourate youtubers upload new videos?
        if yes, who when what is title.
        param: t >> int, time in days.. like 2, 5, 10 etc
        favourateYoutubers >> list of link of youtubers page like:
        https://www.youtube.com/user/onemeeeliondollars/videos
        a >> int, How many new videos to check? like if a is 8, it would check
       first 8 videos in channels you mentioned and check time accordingly.'''

    for x in range(0, len(favourateYoutubers)):

        htmlVids = requests.get(favourateYoutubers[x], headers={"Accept-Language": "en-US"}).text
        # print(htmlVids[:5000])
        vidSoup = BeautifulSoup(htmlVids, 'lxml')
        # print(vidSoup.prettify()[:5000])
        author = vidSoup.title.text[2:-11]
        # print()
        print(author)
        allInfo = vidSoup.find_all('div', class_='yt-lockup-content')[:a]
        # print(allInfo)
        for x in allInfo:
            # print(x)
            time_ago = x.li.find_next_sibling('li').text
            sec_ago = convert_to_seconds(time_ago)
            if sec_ago < int(t) * 24 * 60 * 60:
                # author = vidSoup.title.text[2:-11]
                video_title = x.a.text
                vid_url = 'https://www.youtube.com' + x.a.get('href')
                print(video_title + '\n' + time_ago + '\n' + vid_url)
                vids.append(vid_url)
            print()
    return vids


def convert_to_seconds(time):
    t = int(time[0:2])
    if 'minutes' in time:
        return t * 60
    elif 'hour' in time:
        return t * 60 * 60
    elif 'day' in time:
        return t * 24 * 60 * 60
    elif 'week' in time:
        return t * 7 * 24 * 60 * 60
    elif 'month' in time:
        return t * 30 * 24 * 60 * 60
    elif 'year' in time:
        return t * 365 * 30 * 24 * 60 * 60


ashish_chanchlani = 'https://www.youtube.com/user/ashchanchlani/videos'
bb_ki_vines = 'https://www.youtube.com/channel/UCqwUrj10mAEsqezcItqvwEw/videos'
physicsGirl = 'https://www.youtube.com/user/physicswoman/videos'
favourateYoutubers = [ashish_chanchlani, bb_ki_vines, physicsGirl]

video_haru = favYoutubersVid(favourateYoutubers, 3)

# time.sleep(4)
# For opening videos:
# for l in video_haru:
#     driver = webdriver.Chrome('C:/Users/pk202/OneDrive/Desktop/chromedriver/chromedriver.exe')
#     driver.get(l)
#     videlem = driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')
#     time.sleep(2)
#     videlem.click()
