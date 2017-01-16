# -*- coding: utf-8 -*-

from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.http import request
from tutorial.items import *
class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["xici.com"]
    start_urls = [
        "http://www.xicidaili.com/nn/"
]
    headers={
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
}
    def start_requests(self):
        for i in range(1,5):
            yield Request("http://www.xicidaili.com/nn/%s" %i,headers=self.headers,callback=self.parse)

    def parse(self,response):
        ipElement = response.xpath('//table[@id="ip_list"]/tr[@class]/td[2]/text()')
        portElement=response.xpath('//table[@id="ip_list"]/tr[@class]/td[3]/text()')
        items=[]
        for i in range(len(ipElement)):
            ip=ipElement[i].extract()
            port=portElement[i].extract()
            dest=str(ip)+":"+str(port)
            item=TutorialItem()
            item['dest']=dest
            items.append(item)
        return items




