from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests, re

class TorrentSeeds:
    url = 'https://torrentseeds.org/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find(string=re.compile('Upload :')).get_text(strip=True).replace('Upload :', ''))
        self.download = normalizeSize(soup.find(string=re.compile('Download :')).get_text(strip=True).replace('Download :', ''))
        self.ratio = normalizeFloat(soup.find(string=re.compile('Ratio :')).get_text(strip=True).replace('Ratio :', ''))
        self.freeleech_tokens = normalizeInt(soup.find(string=re.compile('Freeleech Tokens :')).next_element.next_element.get_text(strip=True))
        self.bonus_points = normalizeInt(soup.find(string=re.compile('BON:')).next_element.next_element.get_text(strip=True))
