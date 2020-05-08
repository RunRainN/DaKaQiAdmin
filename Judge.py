# -*- coding:utf-8 -*-
"""
判断是否有该成员，有则审核通过（功能2所需操作）
"""

import requests


def judge():
    s = requests.session()
    headers = {"Content-Length": "0",
               "Host": "www.dakaqi.cn",
               "Connection": "Keep-Alive",
               "User-Agent": "94541365-d701-480a-b298-2cd31d49d7fc/8a2d216865a88a4401661ab0e4984376/Android 6.0.1 2.5.1.1",
               "Cookie": "SERVERID=8a715814d06e7275a2b7fded6130aa45|1567821271|1567821242",
               "Cookie2": "$Version=1",
               "Accept-Encoding": "gzip"
               }
    f_name = open(r".\temp\name.txt", "r")
    f_ids = open(r".\temp\ids.txt", "r")
    f_name_source = open("name_source.txt", "r")  # 源名单
    name_source_list = []
    for name_s in f_name_source:
        name_source_list.append(name_s.strip('\n').decode("utf-8-sig").encode("utf-8"))
    member_dict = {}
    for [name, ids] in zip(f_name, f_ids):
        member_dict.update({name.strip('\n'): ids.strip('\n')})
    for name in member_dict.keys():
        print name.decode('utf-8'),
        if name in name_source_list:
            response = s.post(
                "http://www.dakaqi.cn/services/verifier-activity-apply.action?memberId=8a2d216865a88a4401661ab0e4984376&ids=" +
                member_dict[name] + "&status=2",
                headers=headers)
            print response
        else:
            print(u"名单中无此人")
    f_name.close()
    f_ids.close()
    f_name_source.close()
