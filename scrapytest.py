
import scrapy

class TestSpider(scrapy.Spider):
    name = 'testscrapy'
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        Region_list = response.css('a::attr(href)').extract()
        print(type(response))
        print(Region_list)
        yield {'body':Region_list}