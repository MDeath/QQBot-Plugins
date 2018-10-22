# -*- coding: utf-8 -*-

import random

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        pass# bot.SendTo(g, '已加载 repeat')

def onUnplug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已卸载 repeat')

def info_r(contact):
    file = open('.qqbot-tmp/'+contact.name+'/info.txt', 'r', encoding='utf-8')
    text = file.read()
    info = eval(text)
    file.close
    return info

def info_w(contact, member, content, info):
    info['user'].append(member)
    del info['user'][0]
    info['text'].append(content)
    del info['text'][0]
    file_w = open('.qqbot-tmp/'+contact.name+'/info.txt', 'w', encoding='utf-8')
    file_w.write(str(info))
    file_w.close

def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):user_uin = 0
    else:user_uin = member.uin
    if member != None and not bot.isMe(contact, member):
        if random.randint(0,500) < 1:
            bot.SendTo(contact, content)
        else:
            info = info_r(contact)
            user = info['user']
            user.append(user_uin)
            text = info['text']
            text.append(content)
            repeat = 0
            if not 0 in user:
                for _ in user:
                    text_pop = text.pop()
                    if text_pop in text:
                        repeat_text = text_pop
                        repeat += 1
                if repeat == 1 < 1 and random.randint(0,1):
                    bot.SendTo(contact, repeat_text)
    if member != None:
        try:
            info = info_r(contact)
            info_w(contact, user_uin, content, info)
        except:
            try:
                os.mkdir('.qqbot-tmp/'+contact.name)
            except:
                pass
            info = {
                'user': [0, 1, 2, 3, 4],
                'text': [0, 1, 2, 3, 4]}
            info_w(contact, user_uin, content, info)
