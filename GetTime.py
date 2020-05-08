# -*- coding:utf-8 -*-
"""
获取详细志愿时间（功能1所需操作）
"""

import requests
import re


def get_time():
    s = requests.session()
    headers = {"Content-Length": "0",
               "Host": "www.dakaqi.cn",
               "Connection": "Keep-Alive",
               "User-Agent": "94541365-d701-480a-b298-2cd31d49d7fc/8a2d216865a88a4401661ab0e4984376/Android 6.0.1 2.5.1.1",
               "Cookie": "xxx",
               "Cookie2": "$Version=1",
               "Accept-Encoding": "gzip"
               }
    f = open(r".\temp\ID.txt", "r")
    data = f.read().splitlines()
    fn = open("name_total.txt", "r")
    ft = open('time_total.txt', 'w+')
    for [name, ID] in zip(fn, data):
        sum = 0
        for i in range(1, 10):
            text = s.post(
                "http://www.dakaqi.cn/services/other-member-info.action?memberId=" + ID + "&pageNumber=" + str(i),
                headers=headers).content
            date_list = re.compile('"dateTime":"(.*?)"').findall(text)
            time_list = re.compile('"title":"参加了志愿活动,服务时间为(.*?)分钟。"').findall(text)
            for date, time in zip(date_list, time_list):
                ft.write(date + ' ' + time + '\t')
                sum += int(time)
        print name.strip('\n').decode('utf-8', 'ignore').encode('gbk',
                                                                'ignore'),  # .decode('utf-8')这样打包成exe后在控制台下不会中文乱码
        print sum / 60.0
        ft.write('\n')
    f.close()
    fn.close()
    ft.close()
