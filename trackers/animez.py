from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests

class AnimeZ:
    url = 'https://animetorrents.me/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('li', {'class': 'uploaded'}).get_text(strip=True).replace('Up:', ''))
        self.download = normalizeSize(soup.find('li', {'class': 'downloaded'}).get_text(strip=True).replace('Down:', ''))
        self.ratio = normalizeFloat(soup.find('li', {'class': 'ratio-good'}).get_text(strip=True).replace('Ratio:', ''))
        self.bonus_points = normalizeInt(soup.find('strong', string='Bonus:').next_sibling.get_text(strip=True))