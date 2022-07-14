import scrapy
from autoria_tesla.items import CarItem


class AutoriaSpider(scrapy.Spider):
    name = "autoria"
    start_urls = ['https://auto.ria.com/uk/legkovie/tesla/']

    def parse(self, response, **kwargs):
        """This function will collect and save the requested info from site"""
        for car in response.css('div.content'):
            item = CarItem()
            item['model'] = car.css('span::text').get().strip()
            item['year'] = car.css('a::text')[1].get().strip()
            item['mileage'] = car.css('li[class="item-char js-race"]'
                                      '::text').get().strip()
            item['UAH_price'] = car.css('span[data-currency="USD"]'
                                        '::text').get()
            item['USD_price'] = car.css('span[data-currency="USD"]'
                                        '::text').get()
            item['vin_code'] = self.check_vin(car.css('span[class="label-vin"]'
                                                      ' span::text').get())
            item['car_link'] = car.css('a::attr(href)').get()
            yield item

        next_page = response.css('span[class="page-item next text-r"] '
                                 'a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def check_vin(self, vin_extract):
        """This function will check vin code"""
        if not vin_extract:
            return f'Vin-code not specified'
        else:
            return vin_extract
