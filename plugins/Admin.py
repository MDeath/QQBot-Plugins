# -*- coding: utf-8 -*-

import os
import time

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已加载 '+str(__name__))

def onUnplug(bot):
    group = bot.List('group')
    for g in group: bot.SendTo(g, ('本插件 '+str(__name__)+' 不支持卸载'))
    bot.Plug(str(__name__))

def admin_ID(bot, contact, member, code = 0):
    if code >= 1:
        if member != None:
            user_list = bot.List('buddy', 'user')
            for user in user_list:
                if user.uin == member.uin:
                    return True
    if code >= 0:
        admin = bot.List('buddy','Admin')[0]
        if member != None:
            return admin.uin == member.uin
        elif member == None:
            return admin.uin == contact.uin

def onQQMessage(bot, contact, member, content):
    if '菜单' == content:
        info = '''用户指令:
        bot指令:
            bot闭嘴 , 闭嘴bot
            bot说话 , 说话bot
            bot用户 , bot用户 + number
        插件指令:
            插件列表
            加载插件: + 插件名
            卸载插件: + 插件名
            (插件用","分隔)
        成员指令:
            查看ID
            抽奖菜单(加载与否)'''
        bot.SendTo(contact, info)
    if '查看ID' == content:
        if member != None:
            group = bot.List('group', contact.name)[0]
            buddy = bot.List(group, member.name)[0]
            bot.SendTo(contact, str(contact) + '\nUID:' + buddy.uin + '\n昵称：' + buddy.nick + '\n群名片：' +buddy.name)
        elif member == None:
            buddy = bot.List('buddy', contact.name)[0]
            bot.SendTo(contact, 'UID:' + buddy.uin + '\n昵称：' + buddy.nick + '\n群名片：' + buddy.name)
    if ('重启bot' == content or 'bot重启' == content) and admin_ID(bot,contact,member):
        bot.Restar()
    if '更新数据' in content and admin_ID(bot,contact,member, 0):
        if bot.Update('buddy'):
            Updata = True
        elif bot.Update('group'):
            Updata = True
        elif member != None and bot.Update('group',contact):
            Updata = True
        else:
            Updata = False
        if Updata:
            bot.SendTo(contact, '数据更新完成')
        else:
            bot.SendTo(contact, '数据更新')
    if admin_ID(bot,contact,member, 1):
        if 'bot管理员' == content:
            admin = bot.List('buddy', 'Admin')[0]
            bot.SendTo(contact, '管理员：'+admin.nick+' ID:'+admin.uin)
        if '闭嘴bot' == content or 'bot闭嘴' == content:
            lst = os.listdir('.qqbot-tmp\plugins')
            for f in lst:
                if'.py'in f and not('plugMod'in f or'Admin'in f or'INFO'in f):
                    f = f.replace('.py', '')
                    bot.Unplug(f)
        if '说话bot' == content or 'bot说话' == content:
            lst = os.listdir('.qqbot-tmp\plugins')
            for file in lst:
                if '.py' in file:
                    file = file.replace('.py', '')
                    bot.Plug(file)
        if 'bot用户' == content:
            user_list = bot.List('buddy', 'user')
            for user in user_list:
                bot.SendTo(contact,'用户：'+user.nick+'\nID:'+user.uin)
        elif 'bot用户' in content:
            strnum = content.split('bot用户')[1]
            num = int(strnum)
            user = bot.List('buddy', 'user')[num]
            bot.SendTo(contact, '用户'+strnum+'：'+user.nick+'\nID:'+user.uin)