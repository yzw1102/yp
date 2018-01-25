# -*- coding:utf-8 -*-

import urllib.request
import urllib.error
import re
import time
from lxml import etree
page = 1
url = 'http://b2b.huangye88.com/langfang/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
count=0

try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    root = etree.HTML(content);
    links = root.xpath("//div[@class='box ad_L']/descendant::li/a/@href")
    # tradeDirectoryDict = {}
    # for link in links:
    #     tradeDirectoryDict[link.xpath("attribute::href")[0]] = link.xpath("attribute::title")[0]
    print(links)

    # request = urllib.request.Request(list(tradeDirectoryDict.keys())[0], headers=headers)
    # response = urllib.request.urlopen(request)
    # content = response.read().decode('utf-8')
    # root = etree.HTML(content);
    # # print(content)
    # tradeInfoDict={}
    # tradeInfoDts = root.xpath("//div[@class='mach_list2']/form/dl/dt")
    # for dt in tradeInfoDts:
    #     tradeTel = dt.xpath("span/a/text()");
    #     tradeName = dt.xpath("h4/a/text()")
    #     tradeInfoDict[tradeTel[0]] = tradeName[0]
    # print(tradeInfoDict)
    #
    # url2 = "http://b2b.huangye88.com/langfang/jixie/"
    # url3 = "http://b2b.huangye88.com/langfang/hanjieqiege/"
    # url4 = "http://b2b.huangye88.com/langfang/yejin/pn10/"
    # request = urllib.request.Request(url4, headers=headers)
    # response = urllib.request.urlopen(request)
    # content = response.read().decode('utf-8')
    # root = etree.HTML(content);
    # currentPage = 1;
    # pageNumbers = root.xpath("//div[@class='page_tag Baidu_paging_indicator']/span/following-sibling::a[text() !='下一页' and text() != '下10页']/text()")
    # if pageNumbers :
    #     print(pageNumbers)
    #
    # else :
    #     print("empty list")



    # liItems = divItem[0].xpath("descendant::li/a/attribute::href | ")
    # print(len(divItem))
    # print(divItem)


    # for li in liItems:
    #     print(li)

    # print(liItems)
    # time.sleep(2)
    # pattern =re.compile('<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>', re.S)
    # items = re.findall(pattern, content)
    #
    # for item in items:
    #     print("Author:"+item[0])
    #     print("Content:"+ item[1])
    #     print("favourite:"+ item[2])
    #     print("=====================")
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.reason)
else:
    print("Executed!")