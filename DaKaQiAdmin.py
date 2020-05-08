# -*- coding:utf-8 -*-
"""
mail:1121192423@qq.com
"""

import requests
import re
import GetID
import GetTime
import GetApplicant
import Judge
import SetTime


class DaKaQi:
    def __init__(self):
        self.s = requests.session()
        print(u"志愿者打卡器管理员版1.0")
        print(u"---主菜单---")
        print(u"1.查询组织成员的志愿时长")
        print(u"2.活动一键审核")
        print(u"3.活动一键修改时长")
        # 用户输入判断
        while True:
            try:
                print(u"请选择相应功能的序号："),
                num = int(raw_input())
            except (ValueError, ZeroDivisionError):
                print(u"输入有误，请重新选择")
            else:
                if num < 1 or num > 3:
                    print(u"输入有误，请重新选择")
                else:
                    break
        if num == 1:
            self.search_time()
        if num == 2:
            self.check()
        elif num == 3:
            self.set_time()

    def search_time(self):
        print(u"请确保将查询的人员名单写入name_total.txt，并保证其在运行目录下")
        print(u"若人员较多则所需时间较长，请耐心等待...")
        GetID.get_id()
        GetTime.get_time()
        print(u"详细时长已保存在time_total.txt")
        print(u"按任意键返回主菜单..."),
        raw_input()
        self.__init__()

    def check(self):
        print(u"请确保将通过审核的人员名单写入name_source.txt，并保证其在运行目录下")
        text = self.s.post("http://www.dakaqi.cn/services/org-activity-list.action?pageNumber=1&orgId=4903",
                           headers=headers).content
        # print text
        name_list = re.compile('"name":"(.*?)"').findall(text)
        id_list = re.compile('"id":(\d+)').findall(text)
        for [name, id] in zip(name_list, id_list):
            print name.decode('utf-8', 'ignore').encode('gbk', 'ignore'), id
        print(u"请输入活动ID："),
        id = raw_input()
        GetApplicant.get_applicant(id)
        Judge.judge()
        print(u"审核完成，按任意键返回主菜单..."),
        raw_input()
        self.__init__()

    def set_time(self):
        print(u"请确保将通过审核的人员时长写入time_source.txt（顺序要与name_source.txt保持一致），并保证其在运行目录下")
        text = self.s.post("http://www.dakaqi.cn/services/org-activity-list.action?pageNumber=1&orgId=4903",
                           headers=headers).content
        name_list = re.compile('"name":"(.*?)"').findall(text)
        id_list = re.compile('"id":(\d+)').findall(text)
        # print name_list
        for [name, id] in zip(name_list, id_list):
            print name.decode('utf-8', 'ignore').encode('gbk', 'ignore'), id
        print(u"请输入活动ID："),
        id = raw_input()
        SetTime.set_time(id)
        print(u"修改完成,按任意键返回主菜单..."),
        raw_input()
        self.__init__()


if __name__ == '__main__':
    headers = {"Content-Length": "0",
               "Host": "www.dakaqi.cn",
               "Connection": "Keep-Alive",
               "User-Agent": "94541365-d701-480a-b298-2cd31d49d7fc/8a2d216865a88a4401661ab0e4984376/Android 6.0.1 2.5.1.1",
               "Cookie": "SERVERID=8a715814d06e7275a2b7fded6130aa45|1567821271|1567821242",
               "Cookie2": "$Version=1",
               "Accept-Encoding": "gzip"
               }
    D = DaKaQi()
