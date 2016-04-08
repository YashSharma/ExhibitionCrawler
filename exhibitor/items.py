# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExhibitorItem(scrapy.Item):
    #link = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    country = scrapy.Field()
    website = scrapy.Field()
    description = scrapy.Field()