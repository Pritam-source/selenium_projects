import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from time import sleep
from selenium.common.exceptions import NoSuchElementException
class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    def start_requests(self):
        self.driver = webdriver.Chrome('C:/google_driver/chromedriver.exe')
        self.driver.get('http://books.toscrape.com')
        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url =  'http://books.toscrape.com/'+ book  
            yield scrapy.Request(url,callback=self.parse)
        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                sleep(3)
                next_page.click()
                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                for book in books:
                    url =  'http://books.toscrape.com/catalogue/'+ book  
                    yield scrapy.Request(url,callback=self.parse)
                
            except NoSuchElementException:
                self.logger.info("no more pages to load")
                self.driver.quit()
                break


    def parse(self, response):
        for 
