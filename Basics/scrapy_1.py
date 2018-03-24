
# coding: utf-8

# In[2]:


import scrapy

class mofanSpider(scrapy.Spider):
    name = 'mofan'
    start_urls = ['https://morvanzhou.github.io/',]
    
    def parse(self, response):
        yield {
            'title' : response.css('h1::text').extract_first(default = 'Missing').strip().replace('"', ""),
            'url' : response.url,
        }
        
        urls = response.css('a::attr(href)').re(r'^/.+?/$') # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse) # it will filter out duplicate urls automatically

