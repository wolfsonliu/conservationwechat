#-------------------
# Library
#-------------------

import os
import scrapy
import numpy as np
import pandas as pd
from urllib.parse import quote
import time

#-------------------
# Variables
#-------------------

basedir = '/home/zhiheng/Documents/Work/nature/qingchuan/conservationwechat'
htmldir = os.path.join(basedir, 'html')

wxidlist = pd.read_csv(os.path.join(basedir, 'wxid1.csv'), header=None)

wxid = list(wxidlist[2].head(1))
wxname = list(wxidlist[3].head(1))

class WechatSpider(scrapy.Spider):
    name = "wechat"

    def start_requests(self):
        # make url lists
        urls = [
            'http://weixin.sogou.com/weixin?type=2&ie=utf8&query=' +
            quote(x) + '&tsn=0&ft=&et=&interation=&wxid=' +
            y + '&usip=' + quote(x)
            for x, y in zip(wxname, wxid)
        ]
        referers = [
            'http://weixin.sogou.com/weixin?type=2&query=' +
            quote(x) + '&ie=utf8&s_from=input&_sug_=y&_sug_type_='
            for x in wxname
        ]
        # using sogou to search wechat article of certain publisher
        for url, referer in zip(urls, referers):
            time.sleep(np.random.choice(list(range(20, 60))) * 10)
            yield scrapy.Request(
                url=url,
                callback=self.searchsogou,
                headers={'Referer': url}
            )

    def searchsogou(self, response):
        # using sogou to search wechat article of certain publisher
        hrefs = response.css(
            'div.main-left div.news-box ul.news-list li div.txt-box h3 a::attr(href)'
        ).extract()
        for href in hrefs[:1]:
            print(href)
            #time.sleep(np.random.choice(list(range(20, 60))) * 10)
            yield scrapy.Request(
                url=href,
                callback=self.parsewechat,
                headers={'Referer': response.url}
            )
        # next_page = response.css(
        #     'div.main-left div.news-box div.p-fy a.np::attr(href)'
        # ).extract_first()
        # if next_page is not None:
        #     nextpage = 'http://weixin.sogou.com/weixin' + next_page
        #     yield scrapy.Request(
        #         nextpage,
        #         callback=self.searchsogou,
        #         headers={'Referer': response.url}
        #     )

    def parsewechat(self, response):
        # store the wechat artile information
        title = response.css(
            'div.rich_media_inner div.rich_media_area_primary'
        ).xpath(
            '//div[@id="img-content"]'
        ).css(
            'h2::text'
        ).extract_first().strip()
        wechatname = response.css(
            'div.rich_media_inner div.rich_media_area_primary'
        ).xpath(
            '//div[@id="img-content"]'
        ).css(
            'div.rich_media_meta_list a::text'
        ).extract_first().strip()
        filename = os.path.join(
            htmldir,
            os.path.normpath(
                '{0}-{1}.html'.format(wechatname, title)
            )
        )
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

#-------------------
