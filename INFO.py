# -*- coding: utf-8 -*-

import os
import time

def info_r(contact):
    file = open('.qqbot-tmp/'+contact.name+'/info.txt', 'r', encoding='utf-8')
    text = file.read()
    info = eval(text)
    file.close
    return info

def info_w(contact, member, content, info):
    info['user'].append(member.uin)
    del info['user'][0]
    info['text'].append(content)
    del info['text'][0]
    file_w = open('.qqbot-tmp/'+contact.name+'/info.txt', 'w', encoding='utf-8')
    file_w.write(str(info))
    file_w.close

def record(contact, member, content):
    today = time.strftime('%Y-%m-%d', time.localtime())
    log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    info = log_time + ' ' + member.name + '：' + content + '\n'
    try:
        os.mkdir('.qqbot-tmp/' + contact.name + '/log/')
    except:
        pass
    file_w = open('.qqbot-tmp/' + contact.name + '/log/' + today + '.txt', 'a', encoding='utf-8')
    file_w.write(info)
    file_w.close

def onQQMessage(bot, contact, member, content):
    record(contact, member, content)
    if member != None:
        try:
            info = info_r(contact)
            info_w(contact, member, content, info)
        except:
            try:
                os.mkdir('.qqbot-tmp/'+contact.name)
            except:
                pass
            info = {
                'user': [0, 1, 2, 3, member.uin],
                'text': [0, 1, 2, 3, content]}
            info_w(contact, member, content, info)
