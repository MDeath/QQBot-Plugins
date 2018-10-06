# -*- coding: utf-8 -*-

import INFO
import random

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已加载 repeat')

def onUnplug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已卸载 repeat')

def onQQMessage(bot, contact, member, content):
    if not bot.isMe(contact, member) and member != None:
        if random.randint(0,500) < 1:
            bot.SendTo(contact, content)
        elif random.randint(0,1) < 1:
            randint = random.randint(0,4)
            info = INFO.info_r(contact)
            user, user1, user2 = info['user'][0], info['user'][1], info['user'][2]
            user3, user4 = info['user'][3], info['user'][4]
            text, text1, text2 = info['text'][0] , info['text'][1], info['text'][2]
            text3, text4 = info['text'][3], info['text'][4]
            if randint < 2 and user4 != member.uin and content == text4:
                bot.SendTo(contact, content)
            elif randint == 3 and user3 != user4 != member.uin and text4 == text3 != text2:
                bot.SendTo(contact, text4)
            elif randint == 2 and user2 != user3 != member.uin and text3 == text2 != text1:
                bot.SendTo(contact, text3)
            elif randint == 1 and user1 != user2 != member.uin and text2 == text1 != text:
                bot.SendTo(contact, text2)
            elif randint == 0 and user != user1 != member.uin and text == text1:
                bot.SendTo(contact, text1)
