from datetime import datetime
from collections import defaultdict

from pep_parse.constants import (
    BASE_DIR,
    RESULTS_DIR,
    STATUS_FILE_DATE_FORMAT,
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.counts_per_status = defaultdict(int)

    def process_item(self, item, spider):
        self.counts_per_status[item["status"]] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime(STATUS_FILE_DATE_FORMAT)
        result_dir = BASE_DIR / RESULTS_DIR
        result_dir.mkdir(exist_ok=True)

        file_name = f"status_summary_{now}.csv"
        file_path = result_dir / file_name

        with open(file_path, mode="w", encoding="utf-8") as f:
            f.write("Статус,Количество\n")

            for key, value in self.counts_per_status.items():
                f.write(f"{key},{value}\n")

            total = sum(self.counts_per_status.values())
            f.write(f"Total,{total}\n")
