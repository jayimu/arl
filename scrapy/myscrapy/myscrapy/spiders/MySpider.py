import scrapy
class Test1Spider(scrapy.Spider):
    name = 'myscrapy'
    start_urls = [
        'https://geekori.com'
        ]
    def parse(self,response):
        html = response.xpath('/html').extract()[0]
        print(html)