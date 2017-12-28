
import scrapy
from scrapytest.items import ScrapytestItem

spidercount = 0

class TestSpider(scrapy.Spider):
    name = 'testscrapy'
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        global spidercount
        item = ScrapytestItem()
        hrefs = response.css('a::attr(href)').extract()
        item['name'] = response.url
        item['urllist'] = hrefs
        yield item
        spidercount += 1

        for url in hrefs:
            if(spidercount >= 100):
                return
            yield scrapy.Request(url,callback = self.parse)
