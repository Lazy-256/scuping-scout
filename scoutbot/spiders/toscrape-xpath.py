# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://www.autoscout24.ru/lst/suzuki/swift?sort=age&desc=1&doorfrom=2&doorto=3&ustate=N%2CU&size=20&page=1&cy=NL&priceto=100000&pricefrom=2000&version0=sport&atype=C&',
    ]

    def parse(self, response):
        for car in response.xpath('//div[@class="cl-list-elements"]'):
            yield {
                'example': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]//text()').extract(),
                'title': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary-headline"]/div[@class="cldt-summary-titles"]/a[1]/div[@class="cldt-summary-title"]/div[@class="cldt-summary-makemodelversion sc-ellipsis"]//text()').extract_first(),
                #' ' + quote.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary-headline"]/div[@class="cldt-summary-titles"]/a[1]/div[@class="cldt-summary-title"]/div[@class="cldt-summary-makemodelversion sc-ellipsis"]/h2[@class="cldt-summary-version sc-ellipsis"]/text()').extract_first(),
                'url':   car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary-headline"]/div[@class="cldt-summary-titles"]/a[1]/@href').extract_first(),
                'price': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary"]/div[@class="cldt-summary-pricing"]/div[@class="cldt-summary-payment"]/span[@class="cldt-price sc-font-xl sc-font-bold"]/text()').extract_first(),
                'milage': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary"]/div[@class="cldt-summary-vehicle-data"]/ul[1]/li[1]/text()').extract_first(),
                'relize-date': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary"]/div[@class="cldt-summary-vehicle-data"]/ul[1]/li[2]/text()').extract_first(),
                'power': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary"]/div[@class="cldt-summary-vehicle-data"]/ul[1]/li[3]/text()').extract_first(),
                'place-holder': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary"]/div[@class="cldt-summary-vehicle-data"]/ul[1]/li[@data-placeholder=""]/text()').extract_first(),
                'transmission-type': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary"]/div[@class="cldt-summary-vehicle-data"]/ul[1]/li[data-type="transmission-type"]/text()').extract_first(),
                'seller': car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary-seller"]/div[@class="cldf-summary-seller-data"]/div[@class="cldf-summary-seller-company"]/div[1]/div[@class="cldf-summary-seller-company-first-line"]/div[@class="cldf-summary-seller-company-name"]/text()').extract_first(),
                #' ' + car.xpath('./div[@class="cl-list-element cl-list-element-gap"]/div[@class="cldt-summary-full-item"]/div[@class="cldt-summary-full-item-main"]/div[@class="cldt-summary-seller"]/div[@class="cldf-summary-seller-data"]/div[@class="cldf-summary-seller-company"]/div[1]/div[@class="cldf-summary-seller-contact-second-line"]/div[@class="cldf-summary-seller-contact-address"]/span[2]/text()').extract_first(),
            }

        next_page_url = response.xpath(
            '//li[@class="next-page"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
