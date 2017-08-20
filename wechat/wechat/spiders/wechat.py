#-------------------
# Library
#-------------------

import os
import scrapy
import numpy as np
from urllib.parse import quote
import time

#-------------------
# Variables
#-------------------

basedir = '~/Documents/conservationwechat'
htmldir = os.path.join(basedir, 'html')

wxid = [
    'oIWsFt5arTp4-ulJD-JVbZl8pA4c', 'oIWsFt45lw6ydunoNcq0vQWBipd0'
]

wxname = [
    '梁野山保护区', '内乡宝天曼保护区', '吉林龙湾保护区', '老秃顶子保护区', '图牧吉保护区',
    '公别拉河保护区', '王朗自然保护区', '古田山自然保护区', '长青自然保护区', '南岭自然保护区',
    '太白山自然保护区', '昆嵛山自然保护区', '呼伦湖国家级自然保护区', '胜山国家级自然保护区',
    '赛罕乌拉国家级自然保护区', '黄河三角洲自然保护区', '福建戴云山国家级自然保护区', '陕西朱鹮自然保护区',
    '山东昆嵛山国家级自然保护区', '汗马自然保护区', '九龙川自然保护区', '甘肃裕河自然保护区',
    '甘肃白水江国家级自然保护区', '火石寨保护区', '江苏大丰麋鹿保护区', '平安保护区', '包头南海湿地保护区',
    '茂兰保护区三岔河', '美丽的科尔沁保护区', '永春牛姆林保护区', '广西山口红树林保护区', '扎龙自然保护区',
    '青海湖国家级自然保护区', '闾山自然保护区', '武夷山自然保护区', '神农架自然保护区', '贡嘎山自然保护区',
    '卡山自然保护区', '老河沟自然保护区', '白石砬子自然保护区', '毕拉河自然保护区', '天池自然保护区',
    '连南板洞自然保护区', '龙溪虹口自然保护区', '雪宝顶自然保护区', '尕海则岔自然保护区',
    '三门峡黄河湿地保护区', '科尔沁保护区森林公安局', '罗坑保护区', '辉河保护区', '七姊妹山保护区',
    '象头山保护区', '滨州贝壳堤岛保护区', '杭锦旗自然保护区', '河南董寨国家级自然保护区',
    '北京百花山国家级自然保护区', '湖南壶瓶山国家级自然保护区', '青海省祁连山自然保护区',
    '勿角大熊猫自然保护区', '永德大雪山国家级自然保护区', '甘肃多儿自然保护区', '云南乌蒙山国家级自然保护区',
    '山西涑水河自然保护区', '铜壁关自然保护区', '云南云龙天池自然保护区', '祁连山自然保护区森林公安局',
    '广东石门台自然保护区', '赤水桫椤自然保护区', '贵州梵净山国家级自然保护区', '车八岭自然保护区',
    '珲春东北虎保护局', '太平沟自然保护区', '福建闽江河口湿地', '四川九龙山自然保护区管理处', '九寨沟',
    '黄龙', '广东恩平七星坑保护区', '东方红保护区管护站在线', '湖北青龙山恐龙蛋化石群保护区',
    '鄂托克恐龙遗迹化石自然保护区', '广西大桂山鳄蜥国家级自然保护区', '江西庐山国家级自然保护区管理局',
    '毛乌素沙地柏自然保护区管理局', '白音敖包沙地云杉自然保护区', '贵州佛顶山自然保护区',
    '内蒙古乌旦塔拉自然保护区', '三道坑省级自然保护区管理', '黑龙江伊春河源头省级自然保护区',
    '甘肃敦煌西湖国家级自然保护区', '麻阳河自然保护区管理局', '四川蜂桶寨国家级自然保护区',
    '九原区梅力更自然保护区管护中心', '黑龙江多布库尔国家级自然保护区', '中国山西太宽河自然保护区',
    '西双版纳国家级自然保护区管护局', '宁夏哈巴湖国家级自然保护区', '福建君子峰国家级自然保护区',
    '太统崆峒山国家级自然保护区', '贵州茂兰国家级自然保护区', '安徽古井园国家级自然保护区',
    '甘肃安西极旱荒漠自然保护区', '周至自然保护区双庙子保护站', '周至自然保护区小王涧保护站',
    '四川马边大风顶自然保护区', '盐池湾自然保护区', '绥中五花顶省级自然保护区', '山西四县垴省级自然保护区',
    '珠海淇澳担杆岛省级自然保护区', '周至自然保护区安家岐保护站', '周保局板房子保护站',
    '周保局厚畛子保护站', '平武县关坝流域自然保护中心', '白头叶猴', '花坪银杉', '鞍子河保护地',
    '纳板河流域国家级自然保护区', '周保局板房子所', '周保局双庙子所', '周保局黄草坡护林检查站',
    '四川美姑大风顶自然保护区', '宁夏沙坡头自然保护区', '四面山自然保护区', '攀枝花苏铁自然保护区',
    '弄岗保护区', '四川唐家河国家级自然保护区', '挠力河湿地自然保护区', '湖南张家界大鲵国家级自然保护区',
    '山西桑干河省级自然保护区管理局', '云南会泽黑颈鹤国家级自然保护区', '大佳河自然保护区', '五大连池',
    '广西大明山', '秀美南岳', '七星河国家级自然保护区', '蒲洼自然保护区', '中国南麂',
    '锡林郭勒草原国家级自然保护区', '白马雪山滇金丝猴', '镜泊湖', '兴隆山', '广东河源新港省级自然保护区',
    '莫莫格生态旅游景区', '绿映都江堰', '乾安泥林', '米仓山', '达里诺尔', '盐城珍禽自然保护区',
    '广西合浦儒艮保护区', '老秃顶子保护区', '福建深泸湾海底股森林保护区', '稻城亚丁景区', '魅力白芨滩',
    '北京野鸭湖国家湿地公园', '草海湿地', '天山天池之窗', '沙漠精灵野骆驼', '魅力黄龙山', '畬乡湿地',
    '湿地甘州', '神奇金童山', '无量山自然保护区', '走进贺兰山', '浙江乌岩岭', '罗山管理局',
    '湖南东洞庭湖国际重要湿地', '天津北大港湿地', '千湖湿地', '中华鲟', '丰林国家级自然保护区林业公安局',
    '四川卧龙国家级自然保护区', '宜昌中华鲟保护区', '广西桂林海洋山自然保护区'
]

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
                headers={'Referer': referer}
            )

    def searchsogou(self, response):
        # using sogou to search wechat article of certain publisher
        hrefs = response.css(
            'div.main-left div.news-box ul.news-list li div.txt-box h3 a::attr(href)'
        )
        for href in hrefs:
            time.sleep(np.random.choice(list(range(20, 60))) * 10)
            yield scrapy.Request(
                url=href,
                callback=self.parsewechat,
                headers={'Referer': response.url}
            )
        next_page = response.css(
            'div.main-left div.news-box div.p-fy a.np::attr(href)'
        ).extract_first()
        if next_page is not None:
            nextpage = 'http://weixin.sogou.com/weixin' + next_page
            yield scrapy.Request(
                nextpage,
                callback=self.searchsogou,
                headers={'Referer': response.url}
            )

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

#response.css('div.main-left div.news-box ul.news-list li div.txt-box h3 a::attr(href)')

#fetch("https://mp.weixin.qq.com/s?src=11&timestamp=1503148249&ver=340&signature=XYDFElZ*-qHpfHZziWOB-Xs5Mkc7SxjRvpFAunUznOimPNBuogJ5OcAeE3eNrqt18V9Mf7S3qkYBqsYeYAGNIgLCHYZZpZMSOlFH*c33puqMwo-ls6uLlZlGf4u0ZOtK&new=1", headers={'Referer': "http://weixin.sogou.com/weixin?usip=%E6%A2%81%E9%87%8E%E5%B1%B1%E4%BF%9D%E6%8A%A4%E5%8C%BA&query=%E6%A2%81%E9%87%8E%E5%B1%B1%E4%BF%9D%E6%8A%A4%E5%8C%BA&ft=&tsn=0&et=&interation=&type=2&wxid=oIWsFt5arTp4-ulJD-JVbZl8pA4c&page=10&ie=utf8"})

#-------------------
