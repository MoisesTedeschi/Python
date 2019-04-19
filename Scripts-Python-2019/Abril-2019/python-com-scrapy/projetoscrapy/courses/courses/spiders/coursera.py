# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    # Dominios permitidos - São os dominios que a spider pode trabalhar.
    # allowed_domains = ['https://pt.coursera.org']
    start_urls = ['https://pt.coursera.org/']

    def parse(self, response):
        
        self.log("Hello World! Scrapy Project")
