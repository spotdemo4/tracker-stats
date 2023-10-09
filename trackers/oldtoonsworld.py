from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests

class OldToonsWorld:
    url = 'https://oldtoons.world/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('font', {'class': 'color_uploaded'}).next_element.next_element.get_text(strip=True))
        self.download = normalizeSize(soup.find('font', {'class': 'color_downloaded'}).next_element.next_element.get_text(strip=True))
        self.ratio = normalizeFloat(soup.find('font', {'class': 'color_ratio'}).next_element.next_element.get_text(strip=True))