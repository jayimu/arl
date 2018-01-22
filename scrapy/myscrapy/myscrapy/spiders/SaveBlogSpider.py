import scrapy
from bs4 import *
from myscrapy.items import MyscrapyItem
class Test1Spider(scrapy.Spider):
    name = 'saveblogspider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
        ]
    def parse(self,response):

        item = MyscrapyItem()
        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        for section in sectionList:
            bs = BeautifulSoup(section,'lxml')
            articleDict = {}
            a = bs.find('a')
            articleDict['title'] = a.text
            articleDict['href'] = 'https://geekori.com/' + a.get('href')
            p = bs.find('p', class_='excerpt')
            articleDict['abstract'] = p.text
            item['title'] = articleDict['title']
            item['href'] = articleDict['href']
            item['abstract'] = articleDict['abstract']
            break
        return item
