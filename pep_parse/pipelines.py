import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

from pep_parse.settings import DATETIME_FORMAT, DIR_WITH_RESULTS


BASE_DIR = Path(__file__).parent.parent
PEPS_HEAD = ('Статус', 'Количество')
PEPS_TAIL = 'Всего'


class PepParsePipeline:

    def __init__(self):
        self.downloads_dir = BASE_DIR / DIR_WITH_RESULTS
        self.downloads_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.peps_result = defaultdict(int)

    def process_item(self, item, spider):
        self.peps_result[
            item['status']
        ] += 1
        return item

    def close_spider(self, spider):
        with open(self.downloads_dir / (
            f'status_summary_{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv'
        ), 'w', encoding='utf-8') as file:
            csv.writer(
                file, csv.unix_dialect
            ).writerows([
                PEPS_HEAD,
                *self.peps_result.items(),
                (PEPS_TAIL, sum(self.peps_result.values()))
            ])
