import scrapy
from scrapy.http import Request
from yp.items import TradeItem


class YpSpider(scrapy.Spider):
    name = "yp"
    # start_urls = ['http://b2b.huangye88.com/langfang/led/']
    start_urls = ['http://b2b.huangye88.com/langfang/jixie/', 'http://b2b.huangye88.com/langfang/wujin/',
     'http://b2b.huangye88.com/langfang/guolvfenli/', 'http://b2b.huangye88.com/langfang/naihuocailiao/',
     'http://b2b.huangye88.com/langfang/huanbao/', 'http://b2b.huangye88.com/langfang/dianqi/',
     'http://b2b.huangye88.com/langfang/jichuang/', 'http://b2b.huangye88.com/langfang/bengfa/',
     'http://b2b.huangye88.com/langfang/yinshua/', 'http://b2b.huangye88.com/langfang/xiaofang/',
     'http://b2b.huangye88.com/langfang/gongcheng/', 'http://b2b.huangye88.com/langfang/qipei/',
     'http://b2b.huangye88.com/langfang/shuigongye/', 'http://b2b.huangye88.com/langfang/zhiye/',
     'http://b2b.huangye88.com/langfang/dengshi/', 'http://b2b.huangye88.com/langfang/dianzi/',
     'http://b2b.huangye88.com/langfang/jiagong/', 'http://b2b.huangye88.com/langfang/rebeng/',
     'http://b2b.huangye88.com/langfang/tongxin/', 'http://b2b.huangye88.com/langfang/tianjiaji/',
     'http://b2b.huangye88.com/langfang/nuantongkongtiao/', 'http://b2b.huangye88.com/langfang/yiqiyibiao/',
     'http://b2b.huangye88.com/langfang/qicheyongpin/', 'http://b2b.huangye88.com/langfang/qicheweixiubaoyang/',
     'http://b2b.huangye88.com/langfang/guangdian/', 'http://b2b.huangye88.com/langfang/siyinteyin/',
     'http://b2b.huangye88.com/langfang/qiche/', 'http://b2b.huangye88.com/langfang/anfang/',
     'http://b2b.huangye88.com/langfang/baozhuang/', 'http://b2b.huangye88.com/langfang/ershoushebei/',
     'http://b2b.huangye88.com/langfang/taiyangneng/', 'http://b2b.huangye88.com/langfang/zhiguan/',
     'http://b2b.huangye88.com/langfang/hanjieqiege/', 'http://b2b.huangye88.com/langfang/led/',
     'http://b2b.huangye88.com/langfang/wuliushebei/', 'http://b2b.huangye88.com/langfang/jiajuwang/',
     'http://b2b.huangye88.com/langfang/bangong/', 'http://b2b.huangye88.com/langfang/jiaju/',
     'http://b2b.huangye88.com/langfang/it/', 'http://b2b.huangye88.com/langfang/jiudian/',
     'http://b2b.huangye88.com/langfang/yundongxiuxian/', 'http://b2b.huangye88.com/langfang/jiadian/',
     'http://b2b.huangye88.com/langfang/lipin/', 'http://b2b.huangye88.com/langfang/jiaoyuzhuangbei/',
     'http://b2b.huangye88.com/langfang/yinxiangdengguang/', 'http://b2b.huangye88.com/langfang/wanju/',
     'http://b2b.huangye88.com/langfang/baojianpin/', 'http://b2b.huangye88.com/langfang/meirong/',
     'http://b2b.huangye88.com/langfang/fushi/', 'http://b2b.huangye88.com/langfang/fuzhuang/',
     'http://b2b.huangye88.com/langfang/piju/', 'http://b2b.huangye88.com/langfang/zhixie/',
     'http://b2b.huangye88.com/langfang/guwan/', 'http://b2b.huangye88.com/langfang/xiaojiadian/',
     'http://b2b.huangye88.com/langfang/lingshi/', 'http://b2b.huangye88.com/langfang/zhubao/',
     'http://b2b.huangye88.com/langfang/chongwu/', 'http://b2b.huangye88.com/langfang/ershou/',
     'http://b2b.huangye88.com/langfang/yingyin/', 'http://b2b.huangye88.com/langfang/shenghuo/',
     'http://b2b.huangye88.com/langfang/fuwu/', 'http://b2b.huangye88.com/langfang/jiaotongyunshu/',
     'http://b2b.huangye88.com/langfang/guanggao/', 'http://b2b.huangye88.com/langfang/jiaoyu/',
     'http://b2b.huangye88.com/langfang/weixiu/', 'http://b2b.huangye88.com/langfang/wangzhan/',
     'http://b2b.huangye88.com/langfang/xiangmuhezuo/', 'http://b2b.huangye88.com/langfang/wuliu/',
     'http://b2b.huangye88.com/langfang/jinrong/', 'http://b2b.huangye88.com/langfang/chuangye/',
     'http://b2b.huangye88.com/langfang/zhanhui/', 'http://b2b.huangye88.com/langfang/chuanbo/',
     'http://b2b.huangye88.com/langfang/jiancai/', 'http://b2b.huangye88.com/langfang/huagong/',
     'http://b2b.huangye88.com/langfang/nengyuan/', 'http://b2b.huangye88.com/langfang/yejin/',
     'http://b2b.huangye88.com/langfang/biaomianchuli/', 'http://b2b.huangye88.com/langfang/fangdichan/',
     'http://b2b.huangye88.com/langfang/xiangjiao/', 'http://b2b.huangye88.com/langfang/suliao/',
     'http://b2b.huangye88.com/langfang/fangzhi/', 'http://b2b.huangye88.com/langfang/tuliao/',
     'http://b2b.huangye88.com/langfang/chaoyingcailiao/', 'http://b2b.huangye88.com/langfang/shicai/',
     'http://b2b.huangye88.com/langfang/pige/', 'http://b2b.huangye88.com/langfang/gangtie/',
     'http://b2b.huangye88.com/langfang/shiyou/', 'http://b2b.huangye88.com/langfang/boli/',
     'http://b2b.huangye88.com/langfang/weiyu/', 'http://b2b.huangye88.com/langfang/jianzhutaoci/',
     'http://b2b.huangye88.com/langfang/yangzhi/', 'http://b2b.huangye88.com/langfang/shipin/',
     'http://b2b.huangye88.com/langfang/nongji/', 'http://b2b.huangye88.com/langfang/shuiguo/',
     'http://b2b.huangye88.com/langfang/food/', 'http://b2b.huangye88.com/langfang/yuanlin/',
     'http://b2b.huangye88.com/langfang/siliao/', 'http://b2b.huangye88.com/langfang/shuichanyangzhi/',
     'http://b2b.huangye88.com/langfang/nonghua/']

    def parse(self, response):
        # print(response.request.headers['User-Agent'])
        trade_info_dts = response.xpath("//div[@class='mach_list2']/form/dl/dt")
        for dt in trade_info_dts:
            tel = dt.xpath("span/a/text()").extract()
            name = dt.xpath("h4/a/text()").extract()
            if tel:
                item = TradeItem()
                item['name'] = name[0]
                item['tel'] = tel[0]
                yield item
        next_link = response.xpath("//div[@class='page_tag Baidu_paging_indicator']/a[text() ='下一页']/@href").extract()
        if next_link:
            next_link = next_link[0]
            #print(next_link)
            yield Request(next_link, callback=self.parse)
