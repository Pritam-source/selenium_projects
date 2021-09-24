from selenium import webdriver
from scrapy import Spider
from scrapy.selector import Selector
class BooksSpider(Spider):
    name = "books"
    allowed_domains = ['books.toscrape.com']
    def start_requests(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://books.toscrape.com')
        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/'+ book
            yield scrapy.Request(url, callback=self.parse)
    def parse(self,response):
        pass








