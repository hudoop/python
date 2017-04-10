import scrapy

class DmozItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field()
    desc=scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains=["domz.org"]
    start_urls=[
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename=response.url.split("/")[-2]
        with open(filename,'wb')as f:
            f.write(response.body)

scrapy crawl dmoz