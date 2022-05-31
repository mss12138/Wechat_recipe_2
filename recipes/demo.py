import datetime
from pywchat import Sender

def Recipe():
    title = "--------【今日菜谱】--------\n"
    today = datetime.datetime.now()
    Today = "        今天是" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日\n"
    
    that='2022-04-17'
    start_day = datetime.datetime.strptime(that, '%Y-%m-%d')
    num=str((today-start_day).days)
    with open(f'./texts/150.txt', 'r',  encoding='utf-8') as f:
        text=f.read()
    content=title + Today + text
    return content
    

def send(content):
    #设置企业微信发送消息
    cid='ww8661fac8750ba9d9'
    secret='vnkoEYUQ_QBpeJgbL1axWfkdO9QdcfcI9v6YG7eqzfY'
    agentid=1000003
    app = Sender(cid,secret,agentid)
    
    #发送文字信息
    app.send_text(content, touser='MaShuai')




def main():
    text=Recipe()
    send(text)

if __name__ == '__main__':
    main()
