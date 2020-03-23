# -*- coding: utf-8 -*-
import scrapy


class XixidailiSpider(scrapy.Spider):
    name = 'xixidaili'
    allowed_domains = ['xixidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/1']

    def parse(self, response):
        selectors = response.xpath('//tr')
        for selector in selectors:
            ip = selector.xpath('/td[1]/text()').get()
            port = selector.xpath('/td[2]/text()').get()
            print(ip, port)
