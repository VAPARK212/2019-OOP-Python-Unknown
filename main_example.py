# from Emergency_search import *
from hospital_info import *
from get_location import *

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


def get_location():
    local = get_local()
    print(local.local_coord2region())

    region1 = list(local.local_coord2region())[0]
    region2 = list(local.local_coord2region())[1]

    if region1 == '':
        if region2 != '':
            region1 = region2
        else:
            print("위치 조회중 에러 발생")
    return region1


def basic_info(region1):
    hp_data = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?'
    hp_from_add_url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?'

    hospital_data = Hospital_data(hp_data)
    hospital_pos = Hospital_data_from_pos(hp_from_add_url, region1)
    print('페이지 수:' + str(hospital_pos.page_no))
    print(hospital_pos.show_key())

    return hospital_data, hospital_pos


def get_hp_dict(hospital_pos):
    hp_dict = hospital_pos.get_name_list_id()
    return hp_dict


def get_ER_phone(hospital_data, hp_dict):
    ER_phone = hospital_data.get_ERphone_by_HPID(hp_dict)
    return ER_phone


def get_Address(hospital_data, hp_dict):
    Address = hospital_data.get_Address_by_HPID(hp_dict)
    return Address


def get_data_hospital(hospital_data, treatment_in, hp_l_in, hp_dict_in):
    for hp in hp_l_in:
        for i in treatment_in:
            delete = hospital_data.get_info_by_HPID(treatment_name=i, HPID=hp_dict_in[hp])
            if delete:
                hp_l_in.remove(hp)
                hp_dict_in.pop(hp)
                break
    return hp_l_in, hp_dict_in


treatment_list = ['dutyEryn', 'MKioskTy1', 'MKioskTy10', 'MKioskTy11', 'MKioskTy2', 'MKioskTy25', 'MKioskTy3',
                  'MKioskTy4',
                  'MKioskTy5', 'MKioskTy6', 'MKioskTy7', 'MKioskTy8', 'MKioskTy9']
"""
dutyEryn: 응급실 가용 여부 (가능: 1, 불가능: 2)
MKioskTy1: 뇌출혈수술 (가능: Y, 불가능: N, 정보 없음: U)
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

if __name__ == '__main__':
    region1 = get_location()

    hp_data = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?'
    hp_from_add_url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?'
    treatment_list = ['dutyEryn', 'MKioskTy1', 'MKioskTy10', 'MKioskTy11', 'MKioskTy2', 'MKioskTy25', 'MKioskTy3',
                      'MKioskTy4',
                      'MKioskTy5', 'MKioskTy6', 'MKioskTy7', 'MKioskTy8', 'MKioskTy9']

    hospital_data = Hospital_data(hp_data)
    hospital_pos = Hospital_data_from_pos(hp_from_add_url, region1)
    print('페이지 수:' + str(hospital_pos.page_no))
    print(hospital_pos.show_key())

    hp_dict = get_hp_dict(hospital_pos)
    hp_list = list(hp_dict)
    print(hp_list)
    print(hp_dict)
    hp_list, hp_dict = get_data_hospital(hospital_data, treatment_list, hp_list, hp_dict)
    # print(ER_phone)
    # print(Address)
    print(hp_list)
