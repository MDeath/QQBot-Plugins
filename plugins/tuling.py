# -*- coding: utf-8 -*-

import requests
import json

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        pass# bot.SendTo(g, '已加载 tuling')

def onUnplug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已卸载 tuling')

def talk(con,uId):
    s = requests.session()
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    d = {
        "perception": {
            "inputText": {
                "text": con
            }
        },
        "userInfo": {
            "apiKey": "671d38288232419e975752ba191996f5",
            "userId": uId
        }
    }
    data = json.dumps(d)
    request_post = s.post(url, data=data)
    t = eval(request_post.text)
    r = t["results"]
    results = r[0]
    text = results['values']['text']
    return text

def onQQMessage(bot, contact, member, content):
    namelist = ['辣鸡','傻逼','沙雕','SB','傻吊','垃圾','机器人','复读机','狗','受死','寿司','受、死',
                '无名','无明','武器','笑活','笑着活下去','瑜钰','玉玉','renne','玲','小仓朝日','小仓']
    if'@ME'in content:
        for name in namelist:
            if name in content:
                bot.SendTo(contact, member.nick+'你是'+name+'吗？')
                content = ''
    if '[@ME]' in content:
        content.replace('[@ME]', '')
        result = talk(content, member.uin)
        bot.SendTo(contact, result)

if __name__ == '__main__':
    while True:
        post = input('聊天内容：')
        print('RoBot：'+str(talk(post,1)))