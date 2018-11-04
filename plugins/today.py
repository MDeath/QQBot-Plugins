# coding:utf-8

import time
import requests
from Admin import admin_ID
from bs4 import BeautifulSoup as BS
from qqbot import qqbotsched

def onPlug(bot):
    group = bot.List('group')
    for g in group:
        pass# bot.SendTo(g, '已加载 '+str(__name__))

def onUnplug(bot):
    group = bot.List('group')
    for g in group:
        bot.SendTo(g, '已卸载 '+str(__name__))

@qqbotsched(hour = '4')
def mytask(bot):
    text = todayonhistory()
    gl = bot.List('group')
    if gl is not None:
        for group in gl:bot.SendTo(group, text)

def todayonhistory(today=None):
    if today == None:
        today = time.strftime('%m=%d-', time.localtime())
    today = today.replace('0', '')
    today = today.replace('=', '月')
    today = today.replace('-', '日')
    if '月' not in today or '日' not in today:
        return '格式错误:请以M月D日为格式'
    baidu_baike_url = "https://baike.baidu.com/item/"
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    r = requests.get(url=baidu_baike_url+today,headers=headers)
    r.raise_for_status()
    r.encoding = 'utf-8'
    soup = BS(r.text,'html.parser')
    soup = soup.find('div',{'class':'main-content'})
    history_list = soup.find_all('div',{'class':'para'})
    text = ''
    for history in history_list:
        text += history.text + '\n'
    info_list = text.splitlines()
    text = '历史上的' + today
    for info in info_list:
        if '' != info:
            text += '\n' + info
    return text

def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):
        contact = ''
    if '今天' == content or '历史上的今天' == content:
        if admin_ID(bot, contact, member, 1):
            bot.SendTo(contact, todayonhistory())
        else:
            bot.SendTo(contact, '我警告你别搞事啊')
    if '历史上的' in content:
        if admin_ID(bot, contact, member, 1):
            bot.SendTo(contact, todayonhistory(content.split('历史上的')[1]))
        else:
            bot.SendTo(contact, '我警告你别搞事啊')