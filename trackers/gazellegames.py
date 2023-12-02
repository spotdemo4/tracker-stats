from .utils import convertSize, normalizeSize, normalizeFloat
import requests

class GazelleGames:
    url = 'https://gazellegames.net/'

    def get_api(self, api_key, user_id):
        session = requests.session()
        session.headers.update({'X-API-Key': api_key})

        data = session.get(self.url + f'api.php?request=user&id={user_id}').json()
        print(data)
        self.upload = normalizeSize(convertSize(data['response']['stats']['uploaded']))
        self.download = normalizeSize(convertSize(data['response']['stats']['downloaded']))
        self.ratio = normalizeFloat(data['response']['stats']['ratio'])