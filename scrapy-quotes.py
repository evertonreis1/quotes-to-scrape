import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'QuotesSpider'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('*//div[@class="quote"]')
        for q in quotes:

            yield{

                'title': q.xpath('.//span[@class="text"]/text()').get(),
                'author': q.xpath('.//small[@itemprop="author"]/text()').get(),
                'tags': q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall(),
                
            }

next_pag = response.xpath('*//li[@class="next"]/a/@href').get()

if next_pag is not None:
      yield scrapy.Request(response.urljoin(next_pag), callback=self.parse)