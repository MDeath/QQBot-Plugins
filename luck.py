# -*- coding: utf-8 -*-

import Admin
import os
import time
import random

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已加载 luck')

def onUnplug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已卸载 luck')

def log_write(contact, member, mod, log):
    try:
        os.mkdir('.qqbot-tmp/'+contact.name+'/'+mod+' log')
    except:
        pass
    log_w = open('.qqbot-tmp/'+contact.name+'/'+mod+' log/'+member.nick+'.txt', 'w')
    log_w.write(str(log))
    log_w.close()

def log_read(bot, contact, member, mod):
    today = time.strftime('%Y-%m-%d', time.localtime())
    try:
        log = open('.qqbot-tmp/'+contact.name+'/'+mod+' log/'+member.nick+'.txt', 'r')
        log_r = log.read()
        log.close()
        log = eval(log_r)
        log_today = log['today']['Y:M:D']
        number = log['today']['number']
    except:
        log = {}
        log['name'] = member.nick
        log['last'] = 10
        log['today'] = {'Y:M:D':today, 'number':20}
        log['log'] = []
        for number in range(0,10):
            log['log'].append({'time': '', 'prop': ''})
        log_write(contact, member, mod, log)
        log_today = today
        number = 20
    if today != log_today:
        number += 20
        log['today']['Y:M:D'], log['today']['number'] = today, number
        log_write(contact, member, mod, log)
    if Admin.admin_ID(bot, contact, member)or Admin.user_ID(bot,member):
        log['today']['number'] = 10
    return log

def Luck(bot, contact, member ,mod):
    today = time.strftime('%Y-%m-%d', time.localtime())
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    info = 'None'
    log = log_read(bot, contact, member, mod)
    number, last = log['today']['number'], log['last']
    try:
        file = open('.qqbot-tmp/UP/' + mod, 'r')
        up = file.read()
        file.close()
        set_up = eval(up)
    except:
        try:
            os.mkdir('.qqbot-tmp/UP/')
        except:
            pass
        open('.qqbot-tmp/UP/' + mod, 'a')
        info, number = '未设置UP', -1
    if number > 0:
        number -= 1
        if last > 1:
            last -= 1
            randint = random.randint(1, set_up['full'])
        else:
            randint = random.randint(1, set_up['last_full'])
            last = 10
        initital, full = 0, 0
        for num in set_up['goods_list']:
            full += num['chance']
            if initital < randint <= full:
                Goods_list = num['list']
                info = Goods_list[random.randint(0, len(Goods_list) - 1)]
            initital += num['chance']
        log['last'] = last
        log['today']['Y:M:D'] = today
        log['today']['number'] = number
        log['log'].append({'time': log_time, 'prop': info})
        del log['log'][0]
        log_write(contact, member, mod, log)
        number = True
    elif member == 0:
        number = False
    return info,number

def onQQMessage(bot, contact, member, content):
    if '抽奖菜单' == content:
        info = '''抽奖菜单:
        标配补给
        10连 或 十连 + 标配补给
        查看 + 标配补给 + 记录
        装备补给
        10连 或 十连 装备补给
        查看 + 装备补给 + 记录
        精准补给 A 或 B
        10连 或 十连 精准补给 A 或 B
        查看 + 精准补给 A 或 B
        精准补给 A 或 B + 记录'''
        bot.SendTo(contact, info)
    if not bot.isMe(contact, member) and '标配补给' in content and member!=None:
        mod = 'Avatar'
        if '10连' in content or '十连' in content:
            num, number = 10, True
            message = '十连标配：'
            while num > 0 and number:
                info,number = Luck(bot, contact, member, mod)
                num -= 1
                message += '\n'+info
            else:
                if not number:
                    message += '\n' + member.name + '今天次数已用尽'
            bot.SendTo(contact,message)
        elif '标配补给' == content:
            info, number = Luck(bot, contact, member, mod)
            if number:
                bot.SendTo(contact, info)
            else:
                bot.SendTo(contact, member.name+'今天次数已用尽')
        elif '记录' in content or '查看' in content:
            log = log_read(bot, contact, member, mod)
            last, log_list = log['last'], log['log']
            log_today, number = log['today']['Y:M:D'], log['today']['number']
            log = member.nick+' 今日剩余:'+str(number)+'\n距保底:'+str(last)+'\n'+log_today+'十连:'
            for num in log_list:
                log += '\n'+num['time']+' '+num['prop']
            bot.SendTo(contact, log)

    if not bot.isMe(contact, member) and '装备补给' in content and member!=None:
        mod = 'Weapon'
        if '10连' in content or '十连' in content:
            num, number = 10, True
            message = '十连装备：'
            while num > 0 and number:
                info,number = Luck(bot, contact, member, mod)
                num -= 1
                message += '\n'+info
            else:
                if not number:
                    message += '\n' + member.name + '今天次数已用尽'
            bot.SendTo(contact,message)
        elif '装备补给' == content:
            info, number = Luck(bot, contact,member,mod)
            if number:
                bot.SendTo(contact, info)
            else:
                bot.SendTo(contact, member.name+'今天次数已用尽')
        elif '记录' in content or '查看' in content:
            log = log_read(bot, contact, member, mod)
            last, log_list = log['last'], log['log']
            log_today, number = log['today']['Y:M:D'], log['today']['number']
            log = member.nick+' 今日剩余:'+str(number)+'\n距保底:'+str(last)+'\n'+log_today+'十连:'
            for num in log_list:
                log += '\n'+num['time']+' '+num['prop']
            bot.SendTo(contact, log)

    if not bot.isMe(contact, member) and '精准补给' in content and member!=None:
        if 'A' in content or 'a' in content:
            mod = 'Upweapon A'
        elif 'B' in content or 'b' in content:
            mod = 'Upweapon B'
        else:
            bot.SendTo(contact, '请指明A，B补给')
            content = ''
        if '10连' in content or '十连' in content:
            num, number = 10, True
            message = '十连精准：'
            while num > 0 and number:
                info,number = Luck(bot, contact, member, mod)
                num -= 1
                message += '\n'+ info
            else:
                if not number:
                    message += '\n' + member.name + '今天次数以用尽'
            bot.SendTo(contact,message)
        elif '记录' in content or '查看' in content:
            log = log_read(bot, contact, member, mod)
            last, log_list = log['last'], log['log']
            log_today, number = log['today']['Y:M:D'], log['today']['number']
            log = member.nick+' 今日剩余:'+str(number)+'\n距保底:'+str(last)+'\n'+log_today+'十连:'
            for num in log_list:
                log += '\n'+num['time']+' '+num['prop']
            bot.SendTo(contact, log)
        elif '精准补给' in content:
            info, number = Luck(bot, contact,member,mod)
            if number:
                bot.SendTo(contact, info)
            else:
                bot .SendTo(contact, member.name + '今日次数以用尽')

    if not bot.isMe(contact, member) and '扩充补给' in content and member!=None:
        mod = 'Upavatar'
        if '10连' in content or '十连' in content:
            num, number = 10, True
            message = '十连扩充：'
            while num > 0 and number:
                info,number = Luck(bot, contact, member, mod)
                num -= 1
                message += '\n'+ info
            else:
                if not number:
                    message += '\n' + member.name + '今天次数以用尽'
            bot.SendTo(contact,message)
        elif '记录' in content or '查看' in content:
            log = log_read(bot, contact, member, mod)
            last, log_list = log['last'], log['log']
            log_today, number = log['today']['Y:M:D'], log['today']['number']
            log = member.nick+' 今日剩余:'+str(number)+'\n距保底:'+str(last)+'\n'+log_today+'十连:'
            for num in log_list:
                log += '\n'+num['time']+' '+num['prop']
            bot.SendTo(contact, log)
        elif '扩充补给' in content:
            info, number = Luck(bot, contact,member,mod)
            if number:
                bot.SendTo(contact, info)
            else:
                bot .SendTo(contact, member.name + '今日次数以用尽')