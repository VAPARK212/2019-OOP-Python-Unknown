from kakao_api import *


class Kakao_local_api(Kakao_api):
    def url_maker(self, url):
        return 'https://dapi.kakao.com' + url