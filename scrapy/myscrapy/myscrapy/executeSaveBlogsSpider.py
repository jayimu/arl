from scrapy import cmdline
cmdline.execute('scrapy crawl saveblogsspider -o blogs.json'.split())
