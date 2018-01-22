import scrapy
class Test1Spider(scrapy.Spider):
    name = 'firstscrapy'
    start_urls = [
        'https://geekori.com'
        ]
    def parse(self,response):
        self.log('hello world')