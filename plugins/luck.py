# -*- coding: utf-8 -*-

import os
import time
import random
import requests
import traceback
from Admin import admin_ID
from bs4 import BeautifulSoup as BS

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        pass# bot.SendTo(g, '已加载 luck')

def onUnplug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已卸载 luck')

def log_write(contact, member, mod, log):
    try:os.mkdir('.qqbot-tmp/'+contact.name+'/'+mod+' log')
    except:pass
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
        log['log'] = [{'time': '', 'prop': ''}] * 10
        log_write(contact, member, mod, log)
        log_today = today
        number = 20
    if today != log_today:
        number += 20
        log['today']['Y:M:D'], log['today']['number'] = today, number
        log_write(contact, member, mod, log)
    if admin_ID(bot, contact, member, 1):
        log['today']['number'] = 10
    return log

def set_read(mod):
    try:
        file = open('.qqbot-tmp/UP/' + mod, 'r', encoding='utf-8')
        up = file.read()
        file.close()
        set_up = eval(up)
    except:
        print('traceback.print_exc():', traceback.print_exc())
        try:os.mkdir('.qqbot-tmp/UP/')
        except:pass
        open('.qqbot-tmp/UP/' + mod, 'a')
        set_up = False
    return set_up

def weapon_updata(url):
    if 'https://mp.weixin.qq.com' not in url:return '请用微信公众号的网址'
    request = requests.get(url).text
    soup = BS(request,'lxml')
    title = soup.find('title').text
    if '精准目标确认' not in title:return '网址错误'
    mod, AB = None, None
    data = {
        'url': url,
        'Upweapon A':{
            'weapon':{
                'up':[],
                'list':[]
            },
            'mark':{
                'up':[],
                'list':[]
            }
        },
        'Upweapon B':{
            'weapon':{
                'up':[],
                'list':[]
            },
            'mark':{
                'up':[],
                'list':[]
            }
        },
        'info':title
    }
    titleAB = title.split('」「')
    try:
        for p in soup.find_all('p'):
            text = p.text
            if '精准A补给内容' in text:
                AB = 'Upweapon A'
                title = titleAB[0] + titleAB[1]
                data['info'] += text + '\n'
                continue
            if '精准B补给内容' in text:
                AB = 'Upweapon B'
                title = titleAB[2] + titleAB[3]
                data['info'] += '\n' + text + '\n'
                continue
            if '\xa0' in text:text = text.replace('\xa0','')
            if ' ' in text:text = text.replace(' ','')
            if '：' in text:text = text.replace('：',':')
            if ':' in text:text = text.split(':')[1]
            if '【★4武器】' in text:
                mod = 'weapon'
                data['info'] += text + '\n'
                continue
            if '【★4圣痕】' in text:
                mod = 'mark'
                data['info'] += '\n' + text + '\n'
                continue
            if text == '':
                mod = None
                continue
            if mod != None:data['info'] += text + '\n'
            if mod == 'weapon':
                if '|' in text:
                    for weapon in text.split('|'):
                        if weapon in title:
                            data[AB]['weapon']['up'] = ['4星 ' + weapon]
                        else:
                            data[AB]['weapon']['list'].append('4星 ' + weapon)
                elif text in title:
                    data[AB]['weapon']['up'] = ['4星 ' + text]
                elif text not in title:
                    data[AB]['weapon']['list'].append('4星 ' + text)
            if mod == 'mark':
                if '（' in text:text = text.replace('（','(')
                if '(' in text:text = text.split('(')[0]
                if text in title:UP = True
                else:UP = False
                for num in ['上','中','下']:
                    if '·' in text:
                        for mark in text.split('·'):
                            if mark in title:
                                data[AB]['mark']['up'].append('4星 ' + text + ' ' + num)
                                break
                        else:data[AB]['mark']['list'].append('4星 ' + text + ' ' + num)
                    elif UP:data[AB]['mark']['up'].append('4星 ' + text + ' ' + num)
                    elif text not in title:data[AB]['mark']['list'].append('4星 ' + text + ' ' + num)
    except:
        print('error:', traceback.print_exc())
        return '模板错误'
    return data

def updta_save(data, AB):
    dataAB = set_read(AB)
    if not dataAB:
        dataAB = {
            'url': '',
            'full' : 100000,
            'last_full' : 12395,
            'goods_list' : [
                {
                    'chance' : 2479,
                    'list' : [
                        ''
                    ]
                },
                {
                    'chance' : 3720,
                    'list' : [
                        ''
                    ]
                },
                {
                    'chance' : 2479,
                    'list' : [
                        ''
                    ]
                },
                {
                    'chance' : 3717,
                    'list' : [
                        ''
                    ]
                },
                {
                    'chance' : 11231,
                    'list' : [
                        '3星 双枪 水妖精I型',
                        '3星 双枪 水妖精II型',
                        '3星 双枪 火妖精I型',
                        '3星 双枪 火妖精II型',
                        '3星 太刀 苗刀.电魂',
                        '3星 太刀 苗刀.雷妖',
                        '3星 太刀 脉冲太刀17式',
                        '3星 太刀 脉冲太刀19式',
                        '3星 重炮 马尔科夫A型',
                        '3星 重炮 马尔科夫C型',
                        '3星 重炮 阴极子炮07式',
                        '3星 重炮 阴极子炮09式',
                        '3星 大剑 超重剑.冲锋',
                        '3星 大剑 电离共振剑',
                        '3星 大剑 氮素结晶剑',
                        '3星 大剑 超重剑.王蛇',
                        '3星 十字架 雷天使',
                        '3星 十字架 黑色粉碎者',
                        '3星 十字架 火天使',
                        '3星 拳套 CAS-X圣徒',
                        '3星 拳套 白星驱逐者'
                    ]
                },
                {
                    'chance' : 33694,
                    'list' : [
                        '3星 呼邪 上',
                        '3星 呼邪 中',
                        '3星 呼邪 下',
                        '3星 阿提拉 上',
                        '3星 阿提拉 中',
                        '3星 阿提拉 下',
                        '3星 坂本龙马 上',
                        '3星 坂本龙马 中',
                        '3星 坂本龙马 下',
                        '3星 奥吉尔 上',
                        '3星 奥吉尔 中',
                        '3星 奥吉尔 下',
                        '3星 查理曼 上',
                        '3星 查理曼 中',
                        '3星 查理曼 下',
                        '3星 尼古拉.特斯拉 上',
                        '3星 尼古拉.特斯拉 中',
                        '3星 尼古拉.特斯拉 下',
                        '3星 巴托里.伊丽莎白 上',
                        '3星 巴托里.伊丽莎白 中',
                        '3星 巴托里.伊丽莎白 下',
                        '3星 里纳尔多 上',
                        '3星 里纳尔多 中',
                        '3星 里纳尔多 下',
                        '3星 时雨绮罗 上',
                        '3星 时雨绮罗 中',
                        '3星 时雨绮罗 下',
                        '3星 伽利略 上',
                        '3星 伽利略 中',
                        '3星 伽利略 下',
                        '3星 芥川龙之介 上',
                        '3星 芥川龙之介 中',
                        '3星 芥川龙之介 下'
                    ]
                },
                {
                    'chance' : 17072,
                    'list' : [
                        '材料 特斯拉涡轮机',
                        '材料 相转移镜面',
                        '材料 超合金盾',
                        '材料 超小型反应炉',
                        '材料 断裂的刀柄',
                        '材料 铱合金火星塞'
                    ]
                },
                {
                    'chance' : 17072,
                    'list' : [
                        '经验 双子以太碎片',
                        '经验 以太结晶',
                        '经验 双子以太结晶',
                        '经验 双子灵魂碎片',
                        '经验 灵魂结晶',
                        '经验 双子灵魂结晶'
                    ]
                },
                {
                    'chance' : 8536,
                    'list' : [
                        '金币 吼咪宝藏',
                        '金币 吼美宝藏',
                        '金币 吼里宝藏'
                    ]
                }
            ]
        }
    dataAB['url'] = data['url']
    dataAB['goods_list'][0]['list'] = data[AB]['weapon']['up']
    dataAB['goods_list'][1]['list'] = data[AB]['mark']['up']
    dataAB['goods_list'][2]['list'] = data[AB]['weapon']['list']
    dataAB['goods_list'][3]['list'] = data[AB]['mark']['list']
    try:
        file = open('.qqbot-tmp/UP/' + AB, 'w', encoding='utf-8')
    except:
        try:os.mkdir('.qqbot-tmp/UP/')
        except:pass
        file = open('.qqbot-tmp/UP/' + AB, 'w', encoding='utf-8')
    file.write(str(dataAB))
    file.close()

def luck(set_up, randint):
    initital, full = 0, 0
    for num in set_up['goods_list']:
        full += num['chance']
        if initital < randint <= full:
            Goods_list = num['list']
            info = Goods_list[random.randint(0, len(Goods_list) - 1)]
        initital += num['chance']
    return info

def supply(bot, contact, member ,mod):
    today = time.strftime('%Y-%m-%d', time.localtime())
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    info = 'None'
    log = log_read(bot, contact, member, mod)
    number, last = log['today']['number'], log['last']
    set_up = set_read(mod)
    if not set_up:
        info, number = '未设置UP', -1
    if number > 0:
        number -= 1
        if last > 1:
            last -= 1
            randint = random.randint(1, set_up['full'])
        else:
            randint = random.randint(1, set_up['last_full'])
            last = 10
        info = luck(set_up, randint)
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
    if '更新补给' in content and admin_ID(bot, contact, member, 1):
        url = content.split('更新补给')[1]
        data = weapon_updata(url)
        if type(data) == 'str':bot.SendTo(contact, data)
        else:
            updta_save(data, 'Upweapon A')
            updta_save(data, 'Upweapon B')
            bot.SendTo(contact, data['info'])
    for text in ['这期up','这期精准','这期UP','本期up','本期UP']:
        if text in content:
            url = set_read('Upweapon A')['url']
            info = weapon_updata(url)['info']
            bot.SendTo(contact, info)
    if not bot.isMe(contact, member) and '标配补给' in content and member!=None:
        mod = 'Avatar'
        if '10连' in content or '十连' in content:
            num, number = 10, True
            message = '十连标配：'
            while num > 0 and number:
                info,number = supply(bot, contact, member, mod)
                num -= 1
                message += '\n'+info
            else:
                if not number:
                    message += '\n' + member.name + '今天次数已用尽'
            bot.SendTo(contact,message)
        elif '标配补给' == content:
            info, number = supply(bot, contact, member, mod)
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
                info,number = supply(bot, contact, member, mod)
                num -= 1
                message += '\n'+info
            else:
                if not number:
                    message += '\n' + member.name + '今天次数已用尽'
            bot.SendTo(contact,message)
        elif '装备补给' == content:
            info, number = supply(bot, contact,member,mod)
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
                info,number = supply(bot, contact, member, mod)
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
            info, number = supply(bot, contact,member,mod)
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
                info,number = supply(bot, contact, member, mod)
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
            info, number = supply(bot, contact,member,mod)
            if number:
                bot.SendTo(contact, info)
            else:
                bot .SendTo(contact, member.name + '今日次数以用尽')

    if ('禁言套餐'in content or'禁言大转盘'in content or'口了'in content)and admin_ID(bot, contact, member, 1):
        mod = 'shut up'
        set_up = set_read(mod)
        randint = random.randint(1, set_up['full'])
        info = luck(set_up, randint)
        bot.SendTo(contact, '禁言'+info)
