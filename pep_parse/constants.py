from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
ALLOWED_DOMAINS = ["peps.python.org"]
START_URLS = ["https://peps.python.org/"]
NAME_SPIDER = "pep"
RESULTS_DIR = "results"
XPATH_GET_STATUS = """//dt[contains(text(),
                "Status")]/following-sibling::*[1]/abbr/text()"""

XPATH_GET_PEP_TITLE = '//*[@id="pep-content"]/h1/text()'
XPATH_GET_ROWS_PEP_TABLE = '//section[@id="numerical-index"]'
CSS_GET_PEPS_LINKS = 'a.pep::attr("href")'
