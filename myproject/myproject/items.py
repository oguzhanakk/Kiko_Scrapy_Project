# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    name = scrapy.Field()
    data_product = scrapy.Field()
    action = scrapy.Field()
    service = scrapy.Field()
    link = scrapy.Field()