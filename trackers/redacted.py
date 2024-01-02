from bs4 import BeautifulSoup
from .utils import normalizeSize, normalizeFloat, normalizeInt, convertSize
import requests

class Redacted:
    url = 'https://redacted.ch/'
    
    def get_api(self, api_key, user_id):
        session = requests.session()
        session.headers.update({'Authorization': f'{api_key}'})

        data = session.get(self.url + f'ajax.php?action=user&id={user_id}').json()
        self.upload = normalizeSize(convertSize(data['response']['stats']['uploaded']))
        self.download = normalizeSize(convertSize(data['response']['stats']['downloaded']))
        self.ratio = normalizeFloat(data['response']['stats']['ratio'])