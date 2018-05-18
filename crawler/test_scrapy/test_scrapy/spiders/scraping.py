## -*- coding: utf-8 -*-
#import scrapy
#from test_scrapy.items import NewsItem
#
#class YnewsSpider(scrapy.Spider):
#    name = "ynews"
##    allowed_domains = ["gunosy.com"]
#
##    start_urls = ['https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D']
#    start_urls = ['https://search.yahoo.co.jp/']
#
#    def parse(self, response):
#        for selectElements in response.css("div.listArea ul.list li"):
#            item = NewsItem()
#            item['title'] = selectElements.css(".ttl::text").extract_first()
#            item['category'] = selectElements.css(".cate::text").extract_first()
#            item['url'] = selectElements.css("a::attr('href')").extract_first()
#            yield item
#
#        next_page = response.css("div.page-link-option > a::attr('href')")
#        if next_page:
#            url = response.urljoin(next_page[0].extract())
#            yield scrapy.Request(url, callback=self.parse)

import scrapy
from test_scrapy.items import SearchItem

class YsearchSpider(scrapy.Spider):
    name = "search"
#    start_urls = ['https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen%E3%80%803D&aq=-1&oq=&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&x=wrt',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=11',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=21',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=31',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=41',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=51'
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=61',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=71',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=81',
#                  'https://search.yahoo.co.jp/search?p=series7+Arne+Jacobsen+3D&aq=-1&ai=VHk7OCB.SU6fb9TA.5q0bA&ts=4415&ei=UTF-8&b=91',
#                  ]
    start_urls = ['https://www.google.co.jp/search?biw=1500&bih=870&ei=ToDsWraiEojB0gS5-aXAAQ&q=arne+jacobsen+series7&oq=arne+jacobsen+series7',
                  'https://www.google.co.jp/search?q=arne+jacobsen+series7&ei=WIHsWvrKB4KP8wWbx4f4DA&start=10&sa=N&biw=1500&bih=870',
                  ]

    def parse(self, response):
        for sel in response.css("div a"):
            item = SearchItem()
            item['title'] = sel.css("a::text").extract_first()
            item['url'] = sel.css("a::attr('href')").extract_first()
            yield item
    
#        next_page = response.css("div.side mod > a::attr('href')")
#        print(next_page)
#        if next_page:
#            url = response.urljoin(next_page[0].extract())
#            yield scrapy.Request(url, callback=self.parse)