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
    if member != None and not bot.isMe(contact, member):
        if random.randint(0,500) < 1:
            bot.SendTo(contact, content)
        elif random.randint(0,1) == 1:
            info = INFO.info_r(contact)
            user, user1, user2 = info['user'][0], info['user'][1], info['user'][2]
            user3, user4 = info['user'][3], info['user'][4]
            text, text1, text2 = info['text'][0] , info['text'][1], info['text'][2]
            text3, text4 = info['text'][3], info['text'][4]
            if user != user1 != user2 != user3 != user4 != member.uin and content == text4 != text != text1 != text2 != text3:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, content)
            elif user != user1 != user2 != user3 != user4 != member.uin and content == text3 != text != text1 != text2 != text4:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, content)
            elif user != user1 != user2 != user3 != user4 != member.uin and content == text2 != text != text1 != text3 != text4:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, content)
            elif user != user1 != user2 != user3 != user4 != member.uin and content == text1 != text != text2 != text3 != text4:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, content)
            elif user != user1 != user2 != user3 != user4 != member.uin and content == text != text1 != text2 != text3 != text4:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, content)
            elif user != user1 != user2 != user3 != user4 != member.uin and text4 == text3 != text != text1 != text2 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text4)
            elif user != user1 != user2 != user3 != user4 != member.uin and text4 == text2 != text != text1 != text3 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text4)
            elif user != user1 != user2 != user3 != user4 != member.uin and text4 == text1 != text != text2 != text3 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text4)
            elif user != user1 != user2 != user3 != user4 != member.uin and text4 == text != text1 != text2 != text3 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text4)
            elif user != user1 != user2 != user3 != user4 != member.uin and text3 == text2 != text != text1 != text4 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text3)
            elif user != user1 != user2 != user3 != user4 != member.uin and text3 == text1 != text != text2 != text4 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text3)
            elif user != user1 != user2 != user3 != user4 != member.uin and text3 == text != text1 != text2 != text4 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text3)
            elif user != user1 != user2 != user3 != user4 != member.uin and text2 == text1 != text != text3 != text4 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text2)
            elif user != user1 != user2 != user3 != user4 != member.uin and text2 == text != text1 != text3 != text4 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, text2)
            elif user != user1 != user2 != user3 != user4 != member.uin and text1 == text != text2 != text3 != text4 != content:
                if random.randint(0,1) == 1:
                    bot.SendTo(contact, )
