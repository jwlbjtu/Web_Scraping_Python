#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:41:07 2018

@author: wenlongjiang
"""

# First Spider
import scrapy

class FirstSpider(scrapy.Spider):
    name = 'FirstSpider'
    
    def start_requests(self):
        urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
        ]
        
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.thml' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename) 
