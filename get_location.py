from requests import get
from kakao_local_api import *

loc = 'https://ipapi.co/'


class get_local(Kakao_local_api):
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
        docs = self.get_json(self.url_maker('/v2/local/geo/coord2region.json'), payload)['documents']
        return docs


if __name__ == '__main__':
    local = get_local()
    print(local.local_coord2region())

