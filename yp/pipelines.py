# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
from yp.settings import EXCEL_PATH
from yp.dbhelper import DBhelper

class YpPipeline(object):
    def process_item(self, item, spider):
        return item


class TradePipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['名称', '电话'])

    def process_item(self, item, spider):
        line = [item['name'], item['tel']]
        self.ws.append(line)
        self.wb.save(EXCEL_PATH)
        return item


class TradeMysqlPipeline(object):
    def __init__(self):
        self.dbhelper = DBhelper()
        pass
    def process_item(self, item, spider):
        sql = "insert into trade (name,tel) VALUE (%s,%s)"
        self.dbhelper.insert(sql,item['name'],item['tel'])
