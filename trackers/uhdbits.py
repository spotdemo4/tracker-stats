from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat
import requests

class UHDBits:
    url = 'https://uhdbits.org/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('li', {'id': 'stats_seeding'}).find('span').string)
        self.download = normalizeSize(soup.find('li', {'id': 'stats_leeching'}).find('span').string)
        self.ratio = normalizeFloat(soup.find('li', {'id': 'stats_ratio'}).find('span', {'class', 'stat'}).get_text(strip=True))