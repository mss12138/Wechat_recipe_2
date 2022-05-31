import datetime
from pywchat import Sender
import requests

def Recipe1():
    title = "--------【今日菜谱】--------\n"
    today = datetime.datetime.now()
    Today = "        今天是" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日\n"
    
    that='2022-04-17'
    start_day = datetime.datetime.strptime(that, '%Y-%m-%d')
    num=str((today-start_day).days)
    with open(f'./recipes/texts/{num}.txt', 'r',  encoding='utf-8') as f: #在GitHub与本地写文件地址的格式不同
        text=f.read()
    copyright="\nRemixed by mss"
    content=title + Today + text + copyright
    return content
    
def send1(content):
    #设置企业微信发送消息
    cid='ww8661fac8750ba9d9'
    secret='vnkoEYUQ_QBpeJgbL1axWfkdO9QdcfcI9v6YG7eqzfY'
    agentid=1000003
    app = Sender(cid,secret,agentid)
    
    #发送文字信息
    # app.send_text(content, touser='MaShuai')
    app.send_text(content)




def Recipe2():
    title = "----------------【今日菜谱】---------------"
    today = datetime.datetime.now()
    Today = "(^_^)/(T_T)今天是" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日(*^o^)人(^o^*)"
    
    that='2022-04-17'
    start_day = datetime.datetime.strptime(that, '%Y-%m-%d')
    num=str((today-start_day).days)
    with open(f'./recipes/texts/{num}.txt', 'r',  encoding='utf-8') as f: #在GitHub与本地写文件地址的格式不同
        l=f.readlines()
    text='<br>'.join(l)
    copyright='Remixed by mss'
    content=title + '<br>' + Today + '<br>'+ text + '<br>' +copyright
    return content

def send2(content):
    #设置微信pushplus发送消息
    token = 'b04d9467b5bd4316bb9105f72d6f8b6f' #在pushplus网站中可以找到
    title= '今天的菜谱来啦！' #改成你要的标题内容
    topic='001'
    url = 'http://pushplus.plus/send?token='+token+'&title='+title+'&content='+content+'&topic='+topic
    return requests.get(url)





def main():
    text1=Recipe1()
    send1(text1)

    text2=Recipe2()
    send2(text2)

if __name__ == '__main__':
    main()
