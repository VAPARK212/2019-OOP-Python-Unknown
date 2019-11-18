from kakao_api import *


class Kakao_local_api(Kakao_api):
    def url_maker(self, url):
        return 'https://dapi.kakao.com' + url

    def local_coord2region(self, input_coord, output_coord, lang):
        pass