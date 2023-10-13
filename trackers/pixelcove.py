from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests

class PixelCove:
    url = 'https://pixelcove.me/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('span', {'id': 'stats_uploaded'}).get_text(strip=True))
        self.download = normalizeSize(soup.find('span', {'id': 'stats_downloaded'}).get_text(strip=True))
        self.ratio = normalizeFloat(soup.find('span', {'id': 'stats_ratio'}).get_text(strip=True))
        self.bonus_points = normalizeInt(soup.find('span', {'id': 'stats_credits'}).get_text(strip=True))