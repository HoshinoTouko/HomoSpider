'''
@File: ImageSpider.py
@Author: HoshinoTouko
@License: (C) Copyright 2014 - 2017, HoshinoTouko
@Contact: i@insky.jp
@Create at: 2017/11/29 15:07
@Desc: 
'''
import json
import WeiboSpider.Core as Core
import numpy as np
import random
import threading

from WeiboSpider.Common import Common as com


class ImageSpider(Core.Core):
    def __init__(self, cookie=''):
        super(ImageSpider, self).__init__(cookie)

    def get_all_image_urls(self, uid):
        img_list = []
        count = 100
        for page in range(1, 21):
            result = json.loads(self.get_html(self.get_url(uid, count, page)))
            for item in result:
                img_id_list = item.get('pic_urls')
                try:
                    ret_img_id_list = item.get('retweeted_status').get('pic_urls')
                except Exception as e:
                    ret_img_id_list = []
                for img in img_id_list + ret_img_id_list:
                    try:
                        print(img.get('thumbnail_pic'))
                        img_list.append(
                            com.get_between(
                                img.get('thumbnail_pic'),
                                'sinaimg.cn/thumbnail/',
                                '.jpg'
                            )
                        )
                    except Exception as e:
                        print(e, img)
        return img_list, list(map(
            lambda x: 'http://wx%d.sinaimg.cn/large/%s.jpg' % (random.randint(1, 4), x),
            img_list
        ))

    def down_imgs(self, img_name, img_list):
        for num in range(len(img_list)):
            com.down_img(
                img_list[num],
                '../results/%s.jpg' % img_name[num]
            )

if __name__ == '__main__':
    imgSpi = ImageSpider('')
    img_name, img_list = imgSpi.get_all_image_urls('Homo厨')
    print(img_name, img_list)
    imgSpi.down_imgs(img_name, img_list)
