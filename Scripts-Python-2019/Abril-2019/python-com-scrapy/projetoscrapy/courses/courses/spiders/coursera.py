# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    allowed_domains = ['https://pt.coursera.org']
    start_urls = ['http://https://pt.coursera.org/']

    def parse(self, response):
        pass
