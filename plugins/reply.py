# -*- coding: utf-8 -*-

from Admin import admin_ID
import os
import time

def onQQMessage(bot, contact, member, content):
    try:
        file = open('.qqbot-tmp/reply/reply.txt', 'r', encoding='utf-8')
        file = file.read()
        text = eval(file)
    except:
        try: os.mkdir('.qqbot-tmp/reply/')
        except: pass
        file = open('.qqbot-tmp/reply/reply.txt', 'a')
        file.close()
        d = {'Answer': '','Question': '','IsEnabled': '','OnlyAdmin': '','Mode': '','TimeDb': ''}
        text = [d]*2
    for reply in text:
        Answer, Question = reply['Answer'], reply['Question']
        IsEnabled, OnlyAdmin, Mod = reply['IsEnabled'], reply['OnlyAdmin'], reply['Mode']
        if IsEnabled == 0:
            continue
        if OnlyAdmin < 2 and not admin_ID(bot, contact, member, OnlyAdmin):
            continue
        if Mod == 0 and Question == content:
            bot.SendTo(contact, Answer)
        elif Mod == 1 and Question in content:
            bot.SendTo(contact, Answer)
