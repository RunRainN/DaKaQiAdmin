# -*- coding:utf-8 -*-
"""
获取成员ID（功能1所需操作）
"""

import requests
import urllib
import re


def get_id():
    s = requests.session()
    headers = {"Content-Length": "0",
               "Host": "www.dakaqi.cn",
               "Connection": "Keep-Alive",
               "User-Agent": "94541365-d701-480a-b298-2cd31d49d7fc/8a2d216865a88a4401661ab0e4984376/Android 6.0.1 2.5.1.1",
               "Cookie": "SERVERID=8a715814d06e7275a2b7fded6130aa45|1567821271|1567821242",
               "Cookie2": "$Version=1",
               "Accept-Encoding": "gzip"
               }
    # name_list = ["倪润雨","严权康"]
    f_name = open("name_total.txt", "r")
    f_ID = open(r".\temp\ID.txt", "w+")
    # for name in name_list:
    for name in f_name:
        name = name.strip('\n')
        # print name
        name_dict = {"realName": name}
        real_name = urllib.urlencode(name_dict)
        # print real_name
        id_url = "http://www.dakaqi.cn/services/org-member-search.action?" + real_name + "&orgId=4903"  # http不能为https
        res = s.post(id_url, headers=headers)
        # print res.text
        ID = re.compile('"memberId":"(.*?)"').search(res.text)
        ids = re.compile('"id":(\d+)').search(res.text)
        try:
            f_ID.write(ID.group(1) + '\n')
        except:
            f_ID.write('\n')
    f_name.close()
    f_ID.close()
