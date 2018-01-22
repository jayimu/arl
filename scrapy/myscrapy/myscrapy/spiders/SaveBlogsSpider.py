import scrapy
from bs4 import *
from myscrapy.items import MyscrapyItem

class Test1Spider(scrapy.Spider):
    name = 'saveblogsspider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
    ]

    def parse(self, response):
        articleList = []

        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        for section in sectionList:
            bs = BeautifulSoup(section, 'lxml')
            item = MyscrapyItem()
            a = bs.find('a')
            p = bs.find('p', class_='excerpt')
            item['title'] = a.text
            item['href'] = p.text
            item['abstract'] = p.text
            articleList.append(item)
        return articleList