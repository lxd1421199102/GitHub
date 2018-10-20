# 从网易云音乐下载歌单歌曲
# 参考了这些网址
# https://blog.csdn.net/Ciiiiiing/article/details/62434438
# https://github.com/kunkun1230/Python-/tree/master/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%20%E4%B8%8D%E5%86%8D%E7%8A%B9%E8%B1%AB%20%E8%AF%84%E8%AE%BA%E5%88%86%E6%9E%90
# https://www.zhihu.com/question/36081767

from selenium import webdriver
from bs4 import BeautifulSoup
import time
# from lxml import etree
import os
import requests
friend = '631829006'
driver = webdriver.Chrome()
driver.set_window_position(20, 40)#打开浏览器窗口的位置
driver.set_window_size(1100, 700)#打开浏览器窗口的大小
# driver.maximize_window()     #全屏打开浏览器
driver.get('https://music.163.com/#/playlist?id={}'.format(friend))
time.sleep(2)
driver.switch_to.frame("g_iframe")
html = BeautifulSoup(driver.page_source, 'lxml')
print(html)
music_html = html.select('div.ttc > span > a')#<a href="/album?id=3292678" title="异类">
# print(music)
music_li = []
k=1
for i in music_html:
    music_id = i['href'].replace('/song?id=','')
    # print(music_id)
    music =requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(music_id))
    music_li.append(music)
cloudmusic = 'D://cloudmusic//'
if not os.path.exists(cloudmusic):
    os.mkdir('cloudmusic')
for li in music_li:
    filename = cloudmusic + str(k) + '.mp3'
    with open(filename, 'wb')as f:
        f.write(li.content)
        k += 1
print(k)



