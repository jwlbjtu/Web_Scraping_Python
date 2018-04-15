# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # Main Fields
    main_headline = Field()
    headline = Field()
    
    # Separate Fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
    
    # Location Fields
    # location = Field()
    
    
class TestItem(scrapy.Item):
    id = Field()
    name = Field()
    description = Field()
    
class MovieItem(scrapy.Item):
    title = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    stars = scrapy.Field()
    popularity = scrapy.Field()