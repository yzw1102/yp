import scrapy
from scrapy.http import Request
from yp.items import TradeItem


class YpSpider(scrapy.Spider):
    name = "yp"
    start_urls = ['http://b2b.huangye88.com/langfang/led/']

    # url = "http://b2b.huangye88.com/langfang/famen107/"

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
