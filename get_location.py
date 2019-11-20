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
        docs = self.get_json(self.url_maker('/v2/local/geo/coord2regioncode.json'), payload)['documents'][0]
        self.x = x
        self.y = y
        return {docs['region_1depth_name'], docs['region_2depth_name']}

    def get_points(self):
        return {self.x, self.y}


if __name__ == '__main__':
    local = get_local()
    print(local.local_coord2region())

