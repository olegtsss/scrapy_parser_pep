import datetime as dt
from collections import defaultdict
from pathlib import Path

from pep_parse.settings import DATETIME_FORMAT, DIR_WITH_RESULTS


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    peps_result = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.peps_result[
            item['status']
        ] += 1
        return item

    def close_spider(self, spider):
        downloads_dir = BASE_DIR / DIR_WITH_RESULTS
        downloads_dir.mkdir(exist_ok=True)
        with open(downloads_dir / (
            f'status_summary_{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv'
        ), mode='w', encoding='utf-8') as file:
            file.write('Статус,Количество\n')
            for key, value in self.peps_result.items():
                file.write(f'{key},{value}\n')
            file.write(f'Total,{sum(self.peps_result.values())}\n')
