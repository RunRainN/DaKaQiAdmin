# -*- coding:utf-8 -*-
"""
设置时长（功能3所需操作）
"""

import requests
import re


def set_time(activity_id):
    s = requests.session()
    headers = {"Content-Length": "0",
               "Host": "www.dakaqi.cn",
               "Connection": "Keep-Alive",
               "User-Agent": "94541365-d701-480a-b298-2cd31d49d7fc/8a2d216865a88a4401661ab0e4984376/Android 6.0.1 2.5.1.1",
               "Cookie": "SERVERID=8a715814d06e7275a2b7fded6130aa45|1567821271|1567821242",
               "Cookie2": "$Version=1",
               "Accept-Encoding": "gzip"
               }
    f_name_source = open("name_source.txt", "r")  # 源名单
    f_time = open("activity_time.txt", "r")  # 源时长（小时）
    time_dict = {}
    for [name_s, time] in zip(f_name_source, f_time):
        time_dict.update(
            {name_s.strip('\n').decode("utf-8-sig").encode("utf-8"): time.strip('\n')})  # 这个编码的坑我服了，python2真难受啊
    # print time_dict
    for i in range(1, 20):
        # 活动报名人员查询的URL，不同活动需要修改activityID
        text = s.post(
            "http://www.dakaqi.cn/services/activity-sign-list.action?pageNumber=" + str(
                i) + "&activityId=" + activity_id,
            headers=headers).content
        name_list = re.compile('"realName":"(.*?)"').findall(text)
        id_list = re.compile('"id":(\d+)').findall(text)
        for [name, id] in zip(name_list, id_list):
            print name.decode('utf-8', 'ignore').encode('gbk', 'ignore'),
            try:
                t = float(time_dict[name])
                if t - int(t) == 0:
                    t = int(t * 60)
                else:
                    t = int(t * 60) + 1
            except:
                t = 1
                print(u"源名单无此人"),
            print t,
            res = s.post(
                "http://www.dakaqi.cn/services/update-member-activity.action?id=" + id + "&time=" + str(
                    t) + "&memberId=8a2d216865a88a4401661ab0e4984376",
                headers=headers).content
            print res.decode('utf-8', 'ignore').encode('gbk', 'ignore')
