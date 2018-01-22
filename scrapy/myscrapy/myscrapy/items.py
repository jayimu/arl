import scrapy

class MyscrapyItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    abstract = scrapy.Field()
