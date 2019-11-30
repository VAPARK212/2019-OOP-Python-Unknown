import requests
from requests import get
from abc import*

loc = 'https://ipapi.co/'


class Kakao_api:
    def __init__(self):
        self.api_key = 'ea01b00367677ce3c9f5208fa6f4a478'

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

# 출처: https://github.com/kadragon/oop_python_ex/blob/master/project_ex/kakao_api.py
# 출처: https://ipapi.co/api/?python#introduction
