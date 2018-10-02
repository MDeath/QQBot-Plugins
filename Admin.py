# -*- coding: utf-8 -*-

import os

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已加载 Admin')

def onUnplug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已卸载 Admin')

def admin_ID(bot, contact, member):
    admin = bot.List('buddy','Admin')[0]
    if member != None:
        return admin.uin == member.uin
    elif member == None:
        return admin.uin == contact.uin

def user_ID(bot,member):
    user_list = bot.List('buddy', 'user')
    for user in user_list:
        if user.uin == member.uin:
            return True

def onQQMessage(bot, contact, member, content):
    if '查看自己' == content:
        group = bot.List('group', '桃源郷')[0]
        buddy = bot.List(group, member.nick)[0]
        bot.SendTo(contact, 'UID:' + buddy.uin + '\n昵称：' + buddy.nick + '\n群名片：' + buddy.name)
    if admin_ID(bot,contact,member):
        if '重启bot' == content or 'bot重启' == content:
            bot.Restart()
        if '更新数据' in content:
            if bot.Update('buddy'):
                Updata = True
                return
            if bot.Update('group'):
                Updata = True
                return
            if member != None and bot.Update('group',contact):
                Updata = True
            if Updata:
                bot.SendTo(contact, '数据更新成功')

    if admin_ID(bot,contact,member) or user_ID(bot,member):
        if 'bot管理员' == content:
            admin = bot.List('buddy', 'Admin')[0]
            bot.SendTo(contact, '管理员：'+admin.nick+' ID:'+admin.uin)
        if '闭嘴bot' == content or 'bot闭嘴' == content:
            lst = os.listdir('.qqbot-tmp\plugins')
            for f in lst:
                if '.py' in f:
                    f = f.replace('.py', '')
                    bot.Unplug(f)
        if '说话bot' == content or 'bot说话' == content:
            pluglist = [
                "Admin",
                "plugMod",
                "questions",
                "repeat",
                "tuling",
                "luck",
                "INFO"
            ]
            for plug in pluglist:
                bot.Plug(plug)
        if 'bot用户' == content:
            user_list = bot.List('buddy', 'user')
            for user in user_list:
                bot.SendTo(contact,'用户：'+user.nick+'\nID:'+user.uin)
        elif 'bot用户' in content:
            strnum = content.split('bot用户')
            num = int(strnum)
            user = bot.List('buddy', 'user')[num]
            bot.SendTo(contact, '用户'+strnum+'：'+user.nick+'\nID:'+user.uin)
