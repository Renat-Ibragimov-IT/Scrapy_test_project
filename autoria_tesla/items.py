# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    """This class described the "CarItem" object"""
    model = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    UAH_price = scrapy.Field()
    USD_price = scrapy.Field()
    vin_code = scrapy.Field()
    car_link = scrapy.Field()
