import scrapy

from pep_parse.constants import (
    NAME_SPIDER,
    ALLOWED_DOMAINS,
    XPATH_GET_STATUS,
    XPATH_GET_PEP_TITLE,
    XPATH_GET_ROWS_PEP_TABLE,
    CSS_GET_PEPS_LINKS,
    START_URLS,
)
from pep_parse.items import PepParseItem
from pep_parse.utils import get_pep_name_and_number


class PepSpider(scrapy.Spider):
    name = NAME_SPIDER
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        rows_table = response.xpath(XPATH_GET_ROWS_PEP_TABLE).css("tr")
        links = rows_table.css(CSS_GET_PEPS_LINKS).getall()[::2]
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.xpath(XPATH_GET_PEP_TITLE).get()
        number, name = get_pep_name_and_number(pep_title)
        data = {
            "number": number,
            "name": name,
            "status": response.xpath(XPATH_GET_STATUS).get(),
        }
        yield PepParseItem(data)
