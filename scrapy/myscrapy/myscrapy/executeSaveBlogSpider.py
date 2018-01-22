from scrapy import cmdline
cmdline.execute('scrapy crawl saveblogspider -o blog.json'.split())
