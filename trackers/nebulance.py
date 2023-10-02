from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests

class Nebulance:
    url = 'https://nebulance.io/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('a', {'id': 'nav_upload'}).get_text(strip=True).replace('Up: ', ''))
        #self.download = normalizeSize(soup.find('li', {'id': 'stats_leeching'}).find('span', {'class': 'stat'}).string)
        #self.ratio = normalizeFloat(soup.find('li', {'id': 'stats_ratio'}).find('span', {'class': 'stat'}).string)
        self.bonus_points = normalizeInt(soup.find('a', {'id': 'nav_credits'}).get_text(strip=True).replace('Cubits: ', ''))