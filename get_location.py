from requests import get
from kakao_api import *

loc = 'https://ipapi.co/'


class get_local(Kakao_api):
    def url_maker(self, url):
        return 'https://dapi.kakao.com' + url

    def local_coord2region(self, input_coord='WGS84', output_coord='WGS84', lang='ko'):
        x = get(loc+'longitude/').text
        y = get(loc+'latitude/').text
        payload = {
            'x': x,
            'y': y,
            'input_coord': input_coord,
            'output_coord': output_coord,
            'lang': lang
        }
        docs = self.get_json(self.url_maker('/v2/local/geo/coord2regioncode.json'), payload)['documents'][0]
        return {docs['region_1depth_name'], docs['region_2depth_name']}

    def get_points(self):
        x = get(loc + 'longitude/').text
        y = get(loc + 'latitude/').text
        return [x, y]


if __name__ == '__main__':
    local = get_local()
    print(local.local_coord2region())

