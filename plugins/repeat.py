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
    try:os.mkdir('.qqbot-tmp/'+contact.name)
    except:pass
    try:
        file = open('.qqbot-tmp/'+contact.name+'/info.txt', 'r', encoding='utf-8')
        text = file.read()
        file.close()
        info = eval(text)
    except:info = [{'user': member, 'text': content}]*5
    return info

def info_w(contact, member, content):
    info = info_r(contact)
    info.append({'user': member, 'text': content})
    del info[0]
    file_w = open('.qqbot-tmp/'+contact.name+'/info.txt', 'w', encoding='utf-8')
    file_w.write(str(info))
    file_w.close()

def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):user_uin = 0
    else:user_uin = member.uin
    if member != None and user_uin != 0:
        if random.randint(1,1000) == 1:
            bot.SendTo(contact, content)
        else:
            try:
                info = info_r(contact)
            except:
                info = [{'user': '', 'text': ''}] * 2
            info.append({'user': member, 'text': content})
            info_last = info.pop(0)['text']
            repeat = 0
            for _ in info:
                info_pop = info.pop()
                if info_pop['user'] == 0 or info_pop['text'] == info_last or repeat == -1:
                    repeat = -1
                    break
                for ls in info:
                    if ls == info_pop:
                        repeat = -1
                        break
                    if ls['text'] == info_pop['text']:
                        repeat_text = info_pop['text']
                        repeat += 2
            if 0 < random.randint(1,10) < repeat:
                bot.SendTo(contact, repeat_text)
    if member != None:
        try:info_w(contact, user_uin, content)
        except:
            try:os.mkdir('.qqbot-tmp/'+contact.name)
            except:pass
            info_w(contact, user_uin, content)