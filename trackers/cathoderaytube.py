from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt
import requests, re

class CathodeRayTube:
    url = 'https://www.cathode-ray.tube/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find(string=re.compile('Up')).next_element.next_element.next_element.get_text(strip=True))
        self.download = normalizeSize(soup.find(string=re.compile('Down')).next_element.next_element.next_element.get_text(strip=True))
        self.ratio = normalizeFloat(soup.find(string=re.compile('Ratio')).next_element.next_element.next_element.get_text(strip=True))
        self.freeleech_tokens = normalizeInt(soup.find(string=re.compile('Tokens')).next_element.next_element.next_element.get_text(strip=True))
        self.bonus_points = normalizeInt(soup.find(string=re.compile('Credits')).next_element.next_element.next_element.get_text(strip=True))
