import scrapy


class ItvacancySpider(scrapy.Spider):
    name = 'itvacancy'
    allowed_domains = ['career.habr.com']
    start_urls = ['https://career.habr.com/vacancies']

#    pages_count = 1
    def start_requests(self):
#        for page in range(1, 1 + self.pages_count):
        url = f'https://career.habr.com/vacancies?type=all'
        yield scrapy.Request(url, callback=self.parse_pages)


    def parse_pages(self, response, **kwargs):
        for href in response.css('.vacancy-card__title::attr("href")').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)

#data-qa="vacancy-title" .bloko-header-1

    def parse(self, response, **kwargs):
        item = {
            'title': response.css('.page-title__title::text').extract_first('').strip()
        }
        yield item
