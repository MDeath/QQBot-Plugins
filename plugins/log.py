# -*- coding: utf-8 -*-

import os
import time

def onUnplug(bot):
    group = bot.List('group')
    for g in group: bot.SendTo(g, ('本插件 '+str(__name__)+' 不支持卸载'))
    bot.Plug(str(__name__))

def onQQMessage(bot, contact, member, content):
    today = time.strftime('%Y-%m-%d', time.localtime())
    log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    info = log_time + ' ' + member.name + '：' + content + '\n'
    try:
        os.mkdir('.qqbot-tmp/' + contact.name + '/log/')
    except:
        pass
    file_w = open('.qqbot-tmp/' + contact.name + '/log/' + today + '.txt', 'a', encoding='utf-8')
    file_w.write(info)
    file_w.close()