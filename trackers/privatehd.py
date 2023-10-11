from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat
import requests

class PrivateHD:
    url = 'https://privatehd.to/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('li', {'title': 'Upload'}).get_text(strip=True))
        self.download = normalizeSize(soup.find('li', {'title': 'Download'}).get_text(strip=True))
        self.ratio = normalizeFloat(soup.find('li', {'title': 'Ratio'}).get_text(strip=True))
        self.bonus_points = normalizeFloat(soup.find('a', string='Bonus:').next_sibling.get_text(strip=True))