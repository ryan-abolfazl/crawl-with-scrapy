from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    rules = (
        Rule(LinkExtractor(allow="catalogue/category/"), callback="parse_item"),
    )

    def parse_item(self, response):
        yield {
          "title": response.css(".product_main h1::text").get(),
        }
