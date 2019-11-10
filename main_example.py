from Emergency_search import *

def print_local_list(data_list):
    for data in data_list:
        print("%s | %s" % (data['place_name'], data['road_address_name']))

local_keyword = input("현재 위치 키워드 입력> ")
Lk = collect_local(local_keyword)
near_local_list = Lk.local_list()   # 검색한 키워드의 주변 위치 정보 리스트
print_local_list(near_local_list)   # 위치 정보 리스트 출력

correct_address = input("정확한 지번 입력> ")    # 사용자가 위의 near_local_list 중에서 하나 선택하여 road_address_name 입력
Ls = emergency_search(correct_address)
data_list = Ls.keyword_find_emergency()

for data in data_list:
    print("%s | %s | %s | %s"%(data['place_name'], data['phone'], data['place_url'], data['road_address_name']))

