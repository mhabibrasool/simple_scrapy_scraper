# Scraping Quote, Author, Tags from ~
# 'https://quotes.toscrape.com'
# Scrapy

import scrapy
from quotespider.items import QuoteItem

class Scraper(scrapy.Spider):
    name = 'alter_quote'
    allowed_domains = [
        'https://quotes.toscrape.com'
    ]
    custom_settings = {
        'FEEDS' : {'data/%(name)s%(time)s.csv': {'format': 'csv',}}
    }

    def start_requests(self):
        for i in range(1, 11):
            yield scrapy.Request(url=f'https://quotes.toscrape.com/page/{i}', callback=self.parse)
            
        
    def parse(self, response):
        listings = response.css('div.quote')
        item = QuoteItem()
        
        for listing in listings:
            item['Title'] = listing.css('span.text::text').get()
            item['Author'] = listing.css('small.author::text').get()
            item['Relative_Tags'] = listing.css('a.tag::text').getall()
            yield item