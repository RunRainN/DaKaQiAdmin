# -*- coding:utf-8 -*-
"""
获取申请成员的信息（名字及id）（功能2所需操作）
"""

import requests
import re


def get_applicant(activity_id):
    s = requests.session()
    headers = {"Content-Length": "0",
               "Host": "www.dakaqi.cn",
               "Connection": "Keep-Alive",
               "User-Agent": "94541365-d701-480a-b298-2cd31d49d7fc/8a2d216865a88a4401661ab0e4984376/Android 6.0.1 2.5.1.1",
               "Cookie": "SERVERID=8a715814d06e7275a2b7fded6130aa45|1567821271|1567821242",
               "Cookie2": "$Version=1",
               "Accept-Encoding": "gzip"
               }
    f_name = open(r".\temp\name.txt", "w+")
    f_ids = open(r".\temp\ids.txt", "w+")
    for i in range(1, 20):
        # 活动报名人员查询的URL，不同活动需要修改activityID，其中visitor需要管理员id，可通过GetID.py获取
        text = s.post(
            "http://www.dakaqi.cn/services/activity-apply-wait-list.action?activityId=" + activity_id + "&pageNumber=" + str(
                i) + "&visitor=8a2d216865a88a4401661ab0e4984376",
            headers=headers).content
        name_list = re.compile('"realName":"(.*?)"').findall(text)
        ids_list = re.compile('"id":(\d+)').findall(text)
        for [name, id] in zip(name_list, ids_list):
            # print name, id
            f_name.write(name + '\n')
            f_ids.write(id + '\n')
    f_name.close()
    f_ids.close()
