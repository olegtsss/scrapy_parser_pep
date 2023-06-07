import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for tr_pep in response.css(
            'section[id="numerical-index"]'
        ).css('tbody').css('tr'):
            href = tr_pep.css('td')[1].css('a::attr(href)').get()
            if href is not None:
                yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'name': page_title[1],
            'number': int(page_title[0].split()[1]),
            'status': response.css(
                'dt:contains("Status") + dd'
            ).css('abbr::text').get()
        }
        yield PepParseItem(data)
