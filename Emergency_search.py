from kakao_api_local import *


k = Kakao_local_api()

# 사용자의 정확한 위치 입력을 유도하기 위하여 위치 키워드 입력을 통해 키워드와 관련된 위치 정보 리스트를 제공한다.
class collect_local:
    def __init__(self, my_local_keyword):
        self.my_local_keyword = my_local_keyword

    def local_list(self):
        data_list = k.local_keyword(self.my_local_keyword)
        return data_list


# 키워드에 관련된 위치 정보 리스트를 제공받은 사용자가 이 리스트들의 address 중 하나를 선택하여 이 address를 기준으로 주변 병원 탐색
class emergency_search:
    def __init__(self, my_local_address):
        self.my_local_address = my_local_address

    def keyword_find_emergency(self):
        data_list = k.local_address(self.my_local_address)
        my_x = data_list[0]['road_address']['x']
        my_y = data_list[0]['road_address']['y']
        data_list = k.local_keyword('병원', x=my_x, y=my_y, sort='distance', radius=10000)

        """
        'place_name': 장소 이름
        'phone': 전화번호
        'place_url': 관련 홈페이지
        'road_address_name': 지번
        'x': x좌표
        'y': y좌표
        (예시)
        for data in data_list:
            print("%s | %s | %s | %s" % (data['place_name'], data['phone'], data['place_url'], data['road_address_name']))
        """

        return data_list
