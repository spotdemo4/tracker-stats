from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests

class IPTorrents:
    url = 'https://iptorrents.com/t'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('div', string='Uploaded').next_sibling.next_sibling.get_text(strip=True))
        self.download = normalizeSize(soup.find('div', string='Downloaded').next_sibling.next_sibling.get_text(strip=True))
        self.ratio = normalizeFloat(soup.find('div', string='Ratio').next_sibling.next_sibling.get_text(strip=True))
        self.bonus_points = normalizeFloat(soup.find('div', string='Bonus Points').next_sibling.next_sibling.get_text(strip=True))