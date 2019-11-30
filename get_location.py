from kakao_api import *


# kakao api를 이용하는 class
class get_local(Kakao_api):
    def url_maker(self, url):
        return 'https://dapi.kakao.com' + url

    # 지역의 좌표를 행정구역정보로 변환하는 함수
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

    # ip api를 통해 추적한 현재 사용자의 위치를 리스트의 형태로 리턴해주는 함수
    def get_points(self):
        return [self.x, self.y]


if __name__ == '__main__':
    local = get_local()
    print(local.local_coord2region())
    print(local.get_points())

# 출처: https://developers.kakao.com/docs/restapi/local#좌표-행정구역정보-변환
