from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt, convertSize
import requests

class Orpheus:
    url = 'https://orpheus.network/'

    def get_stats(self, cookies, headers):
        session = requests.session()
        session.headers.update(headers)
        soup = BeautifulSoup(session.get(self.url, cookies=cookies).text, 'html.parser')

        self.upload = normalizeSize(soup.find('li', {'id': 'stats_seeding'}).find('span', {'class': 'stat'}).string)
        self.download = normalizeSize(soup.find('li', {'id': 'stats_leeching'}).find('span', {'class': 'stat'}).string)
        self.ratio = normalizeFloat(soup.find('li', {'id': 'stats_ratio'}).find('span', {'class': 'stat'}).string)
        self.freeleech_tokens = normalizeInt(soup.find('li', {'id': 'fl_tokens'}).find('span', {'class': 'stat'}).get_text(strip=True))
        bp_pre = soup.find('li', {'id': 'nav_bonus'}).get_text(strip=True)
        self.bonus_points = normalizeInt(bp_pre[bp_pre.find('(')+1:bp_pre.find(')')])
    
    def get_api(self, api_key, user_id):
        session = requests.session()
        session.headers.update({'Authorization': f'token {api_key}'})

        data = session.get(self.url + f'ajax.php?action=user&id={user_id}').json()
        self.upload = normalizeSize(convertSize(data['response']['stats']['uploaded']))
        self.download = normalizeSize(convertSize(data['response']['stats']['downloaded']))
        self.ratio = normalizeFloat(data['response']['stats']['ratio'])