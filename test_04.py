# 从网易云音乐下载歌单歌曲
# 参考了这些网址
# https://blog.csdn.net/Ciiiiiing/article/details/62434438
# https://github.com/kunkun1230/Python-/tree/master/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%20%E4%B8%8D%E5%86%8D%E7%8A%B9%E8%B1%AB%20%E8%AF%84%E8%AE%BA%E5%88%86%E6%9E%90
# https://www.zhihu.com/question/36081767
# from lxml import etree
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os
import lxml

def music_download(music_li,music_name):
    k = 0
    cloudmusic = './cloudmusic/'
    if not os.path.exists(cloudmusic):
        os.mkdir('cloudmusic')
    for li,ji in zip(music_li,music_name):
        filename = cloudmusic + ji + '.mp3'
        with open(filename, 'wb')as f:
            f.write(li.content)
            k += 1
        # print('第{0}首歌:{1}.mp3 下载成功!'.format(k,ji))
    print('一共下载了{}首歌'.format(k))
def music_info (friend):
    driver = webdriver.Chrome()
    driver.set_window_position(20, 40)  # 打开浏览器窗口的位置
    driver.set_window_size(1100, 700)  # 打开浏览器窗口的大小
    # driver.maximize_window()     #全屏打开浏览器
    driver.get('https://music.163.com/#/playlist?id={}'.format(friend))
    time.sleep(10)
    driver.switch_to.frame("g_iframe")
    html = BeautifulSoup(driver.page_source, 'lxml')
    # print(html)
    music_html = html.select('div.ttc > span > a')  # <a href="/album?id=3292678" title="异类">
    music_names = html.select('div.ttc > span > a > b')
    # print(music)
    music_li = []
    music_name = []
    for i,j in zip(music_html,music_names):
        m= j['title']
        music_id = i['href'].replace('/song?id=', '')
        # print(music_id)
        music = requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(music_id))
        music_li.append(music)
        print('{}.mp3 下载成功!'.format(m))
        music_name.append(m)
    return music_li,music_name
if __name__ == "__main__":
    friend = input('请输入你想下载的歌单的id:')
    # friend = '2476344724'
    print('开始下载歌曲...\n================================================')
    start_time = time.time()  # 开始时间
    music_li,music_name= music_info(friend)
    music_download(music_li,music_name)
    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))
    # https: // music.163.com /  # /playlist?id=2477471309







