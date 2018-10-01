# -*- coding: utf-8 -*-

import requests
import Admin
import json

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已加载 tuling')

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
            "apiKey": "填入你的图灵接口",
            "userId": uId
        }
    }
    data = json.dumps(d)
    request_post = s.post(url, data=data)
    t = eval(request_post.text)
    r = t["results"]
    results = r[0]
    values = results['values']
    text = values['text']
    return text

def onQQMessage(bot, contact, member, content):
    if '@ME' in content:
        result = talk(content, member.uin)
        bot.SendTo(contact, result)

if __name__ == '__main__':
    while True:
        post = input('聊天内容：')
        print('RoBot：'+talk(post,1))
