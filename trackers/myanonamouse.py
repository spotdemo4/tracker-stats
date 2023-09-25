from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests, re

class MyAnonamouse:
    url = 'https://www.myanonamouse.net/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('a', {'id': 'uploadedTD'}).get_text(strip=True))
        self.download = normalizeSize(soup.find('a', {'id': 'downloadedTD'}).get_text(strip=True))
        self.ratio = normalizeFloat(soup.find('a', {'id': 'RatioTD'}).get_text(strip=True).replace('Ratio: ', ''))
        self.freeleech_tokens = normalizeInt(soup.find('a', string=re.compile('FL Wedges:')).get_text(strip=True).replace('FL Wedges: ', ''))
        self.bonus_points = normalizeInt(soup.find('a', {'id': 'bonusLink'}).get_text(strip=True).replace('Bonus: ', ''))