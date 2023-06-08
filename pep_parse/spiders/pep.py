import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for tr_pep in response.css('section[id="numerical-index"] tbody tr'):
            href = tr_pep.css('td')[1].css('a::attr(href)').get()
            if href is not None:
                yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        raw_number, name = response.css(
            'h1.page-title::text'
        ).get().split(' – ')
        yield PepParseItem(
            dict(
                name=name,
                number=int(raw_number.split()[1]),
                status=response.css(
                    'dt:contains("Status") + dd'
                ).css('abbr::text').get()
            )
        )
