#from Emergency_search import *
from hospital_info import *

"""
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

district = correct_address.split()
print(district)
for data in data_list:
    print("%s | %s | %s | %s"%(data['place_name'], data['phone'], data['place_url'], data['road_address_name']))

"""
"""
여기서 부터 병원 만지작 코드
"""

hp_data = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?'
hp_from_add_url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?'

hospital_data = Hospital_data(hp_data)
hospital_pos = Hospital_data_from_pos(hp_from_add_url, '서울특별시', '종로구')

print(hospital_pos.show_url())
hp_list = hospital_pos.get_name_list()
ER_phone = hospital_pos.get_ER_phone(hp_list)
Address = hospital_pos.get_detailAdress(hp_list)
hp_dict = hospital_pos.get_name_list_id()
print(hp_list)
print(hp_dict)
print(ER_phone)
print(Address)

treatment_list = ['MKioskTy1', 'MKioskTy10', 'MKioskTy11', 'MKioskTy2', 'MKioskTy25', 'MKioskTy3', 'MKioskTy4',
                  'MKioskTy5', 'MKioskTy6', 'MKioskTy7', 'MKioskTy8', 'MKioskTy9']
"""
MKioskTy1: 뇌출혈수술
MKioskTy10: 신생아
MKioskTy11: 중증화상
MKioskTy2: 뇌경색의재관류
MKioskty25: 응급실
MKioskTy3: 심근경색의재관류
MKioskTy4: 복부손상의수술
MKioskTy5: 사지접합의수술
MKioskTy6: 응급내시경
MKioskTy7: 응급투석
MKioskTy8: 조산산모
MKioskTy9: 정신질환자
"""
hp_info = []
for hp in hp_list:
    info_tmp = []
    for i in treatment_list:
        hospital_data.get_info_by_HPID(treatment_name=i, info=info_tmp, HPID=hp_dict[hp])
    hp_info.append(info_tmp)
print(hp_info)

hospital_data_dict = hospital_data.create_dict(infolist=hp_info, name_list=hp_list)
print(hospital_data_dict)