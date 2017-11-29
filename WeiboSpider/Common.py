'''
@File: Common.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Create at: 2017/11/29 15:11
@Desc: 
'''
import os
import re
import urllib.request


class Common(object):
    @staticmethod
    def get_between(s, start, end):
        return re.search('%s(.*)%s' % (start, end), s).group(1)

    @staticmethod
    def down_img(imgurl, localpath):
        '''A function to save img'''
        if os.path.exists(localpath):
            print('%s exist!' % localpath)
            return
        print(imgurl, localpath)
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'
        }
        request = urllib.request.Request(url=imgurl, headers=headers)
        data = urllib.request.urlopen(request).read()
        img_file = open(localpath, 'wb')
        img_file.write(data)
        img_file.close()
        return