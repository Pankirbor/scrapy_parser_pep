import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.utils import get_pep_name_and_number


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["http://peps.python.org/"]

    def parse(self, response):
        rows_table = response.xpath('//section[@id="numerical-index"]').css("tr")
        links = rows_table.css('a.pep::attr("href")').getall()[::2]
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        string_pep_discription = response.xpath(
            '//*[@id="pep-content"]/h1/text()'
        ).get()
        number, name = get_pep_name_and_number(string_pep_discription)
        data = {
            "number": number,
            "name": name,
            "status": response.xpath(
                '//*[@id="pep-content"]/dl/dd[2]/abbr/text()'
            ).get(),
        }
        yield PepParseItem(data)


# ? pattern = '(?<=- )[\w ]*$'
# * pep-page-section > header > ul > li:nth-child(3)
# * //*[@id="pep-content"]/h1
# * //*[@id="pep-content"]/dl/dd[2]/abbr
# * rows.css('a.pep::attr("href")').getall()
# * links = rows.css('a.pep::attr("href")').getall()[::2]
# * response.xpath('//section[@id="numerical-index"]').css('tr').css('a.pep::attr("href")').getall()[::2]
