# Second Sipder
import scrapy

from Example.items import NewItem

class SecondSpider(scrapy.Spider):
    name = 'secondspider'
    allowed_domains = ['www.superdatascience.com']
    start_urls = ['https://superdatascience.com']
    
    def parse(self, response):
        item = NewItem()
        item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] = self.name
        print(item)
        return item
