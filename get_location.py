from kakao_api import *


class get_local(Kakao_api):
    def url_maker(self, url):
        return 'https://dapi.kakao.com' + url

    def local_coord2region(self, input_coord='WGS84', output_coord='WGS84', lang='ko'):
        payload = {
            'x': self.x,
            'y': self.y,
            'input_coord': input_coord,
            'output_coord': output_coord,
            'lang': lang
        }
        docs = self.get_json(self.url_maker('/v2/local/geo/coord2regioncode.json'), payload)['documents'][0]
        return (docs['region_1depth_name'], docs['region_2depth_name'])

    def get_points(self):
        return [self.x, self.y]


if __name__ == '__main__':
    local = get_local()
    print(local.local_coord2region())

