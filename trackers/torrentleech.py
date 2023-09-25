from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat
import requests

class TorrentLeech:
    url = 'https://www.torrentleech.org/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('div', {'title': 'Uploaded (Seeding)'}).find('span').string)
        self.download = normalizeSize(soup.find('div', {'title': 'Downloaded (Leeching)'}).find('span').string)
        self.ratio = normalizeFloat(soup.find('div', {'title': 'Ratio'}).get_text(strip=True))
        self.bonus_points = normalizeFloat(soup.find('span', {'class': 'total-TL-points'}).string)