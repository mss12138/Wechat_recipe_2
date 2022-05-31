# encoding:utf-8
import datetime
from pywchat import Sender
import requests


def Recipe():
    title = "--------【今日菜谱】--------\n"
    today = datetime.datetime.now()
    Today = "        今天是" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日\n"
    
    that='2022-04-17'
    start_day = datetime.datetime.strptime(that, '%Y-%m-%d')
    num=str((today-start_day).days)
    with open(f'./texts/{num}.txt', 'r',  encoding='utf-8') as f: #在GitHub与本地写文件地址的格式不同
        text=f.read()
    copyright="\nRemixed by mss"
    content=title + Today + text + copyright
    return content


token = 'b04d9467b5bd4316bb9105f72d6f8b6f' #在pushplus网站中可以找到
title= '今天的菜谱来啦！' #改成你要的标题内容
topic='001'
content= Recipe()
url = 'http://pushplus.plus/send?token='+token+'&title='+title+'&content='+content+'&topic='+topic
requests.get(url)


#pushdeer APP推送
base_url='https://api2.pushdeer.com/message/push?pushkey={key}&text={img}&type=image'
pushkey='PDU9921Tk8QOf5LhnJ5Vh7Su9lzgqT4EsFmuS8J5'
# content =Recipe()
content='mashuai'
img='https://cdn.jsdelivr.net/gh/mss12138/image-hosting@master/picx/361.1jeek4x7tocg.jpg'

url=base_url.format(key=pushkey,img=img)
requests.get(url)