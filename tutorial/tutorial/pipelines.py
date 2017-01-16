# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import dbutil

class TutorialPipeline(object):
    mysql=dbutil.Mysql()
    def process_item(self, item, spider):
        insert_sql="insert into ip.ip values (%s)"
        self.mysql.insertOne(insert_sql,[item['dest']])
