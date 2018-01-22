import scrapy
from bs4 import *
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
        ]
    def parse(self,response):
        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        for section in sectionList:
            bs = BeautifulSoup(section,'lxml')
            articleDict = {}
            a = bs.find('a')
            articleDict['title'] = a.text
            articleDict['href'] = 'https://geekori.com/' + a.get('href')
            p = bs.find('p', class_='excerpt')
            articleDict['abstract'] = p.text
            print(articleDict)