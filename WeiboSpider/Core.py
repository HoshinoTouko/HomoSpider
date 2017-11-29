'''
@File: Core.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Create at: 2017/11/29 13:22
@Desc: Weibo Spider Core
'''
import urllib.request
import numpy as np
from urllib.parse import quote
import json
from bs4 import BeautifulSoup

class Core(object):
    def __init__(self, cookie=''):
        self.cookie = cookie

    def get_url(self, uid, count=100, page=1):
        uid = quote(uid)
        return \
            "http://api.t.sina.com.cn/statuses/user_timeline/%s.json?source=2849184197&count=%s&page=%s" % (uid, count, page)

    # TODO: Use weibo.cn to get more weibo
    # Current api cannot get more than 2000 weibo.
    def count_num_of_weibo(self, uid):
        page = 1
        count = 100
        weibo_id_list = np.empty(1, dtype=np.uint16)
        while(1):
            result = self.get_html(self.get_url(uid, count, page))
            obj = json.loads(result)
            err = 0
            for i in obj:
                if not i in weibo_id_list:
                    np.append(weibo_id_list, i.get('id'))
                    print('Add weibo id: %s', i.get('id'))
                else:
                    err += 1
            if err > 99:
                break
            print('Get url: %s' % (self.get_url(uid, count, page)))
            page += 1
        return weibo_id_list.size

    def get_html(self, url):
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'cookie': self.cookie
        }
        request = urllib.request.Request(url, headers=headers)
        return urllib.request.urlopen(request).read()

if __name__ == '__main__':
    cookie = ''
    core = Core(cookie)
    print(len(json.loads(core.get_html(core.get_url('Homo厨')))))
