import requests
from requests import get
from abc import*

loc = 'https://ipapi.co/'

class Kakao_api:
    def __init__(self):
        self.api_key = '74f2836791b7cbaaa18d715326a695f7'

        self.headers = {
            'Authorization': 'KakaoAK ' + self.api_key
        }

        x = get(loc + 'longitude/').text
        y = get(loc + 'latitude/').text
        self.x = x
        self.y = y

    def get_json(self, url, payload):
        return requests.get(url, headers=self.headers, params=payload).json()

    def post_json(self, url, data=None, file=None):
        return requests.post(url, headers=self.headers, data=data, files=file).json()

    @abstractmethod
    def url_maker(self):
        pass
