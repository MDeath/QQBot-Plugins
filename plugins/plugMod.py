# -*- coding: utf-8 -*-

import Admin
import os

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, ('已加载 '+str(__name__)))

def onUnplug(bot):
    group = bot.List('group')
    for g in group: bot.SendTo(g, ('本插件 '+str(__name__)+' 不支持卸载'))
    bot.Plug(str(__name__))

def onQQMessage(bot, contact, member, content):
    if '加载插件' in content and Admin.admin_ID(bot,contact,member, 1):
        if '，' in content:
            content = content.replace('，',',')
        if '：' in content:
            content = content.replace('：',':')
        content = content.split('加载插件:')[1]
        if ',' in content:
            plugs = content.split(',')
            for plug in plugs:
                bot.Plug(plug)
        else:
            bot.Plug(content)
    if '卸载插件'  in content and Admin.admin_ID(bot,contact,member, 1):
        if '：' in content:
            content = content.split('卸载插件：')[1]
        else:
            content = content.split('卸载插件:')[1]
        if '，' in content:
            content.replace('，', ',')
        if ',' in content:
            plugs = content.split(',')
            for plug in plugs:
                bot.Unplug(plug)
        else:
            bot.Unplug(content)
    if '插件列表' == content and Admin.admin_ID(bot,contact,member, 1):
        lst = os.listdir('.qqbot-tmp\plugins')
        info = '插件列表：'
        for f in lst:
            if '.py' in f:
                f = f.replace('.py','')
                info += '\n' + f
        bot.SendTo(contact, info)
