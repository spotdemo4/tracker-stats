from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests

class FileList:
    url = 'https://filelist.io/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find(string='Uploaded').next_element.replace(':\u00a0', ''))
        self.download = normalizeSize(soup.find(string='Downloaded').next_element.replace(':\u00a0', ''))
        self.ratio = normalizeFloat(soup.find(string='Ratio').next_element.get_text(strip=True))
        self.freeleech_tokens = normalizeInt(soup.find(string='Tokens').next_element.get_text(strip=True))
        self.bonus_points = normalizeFloat(soup.find('a', {'href': '/shop.php'}).get_text(strip=True))