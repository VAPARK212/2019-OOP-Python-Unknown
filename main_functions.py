from hospital_info import *
from get_location import *


def get_location():
    """
    사용자의 위치를 IP로 부터 가져오는 코드
    :return:
    """
    local = get_local()
    print(local.local_coord2region())

    region1 = list(local.local_coord2region())[0] #지역구 1. 광범위
    region2 = list(local.local_coord2region())[1] #지역구 2. 세부적

    if region1 == '':
        if region2 != '':
            region1 = region2
        else:
            print("위치 조회중 에러 발생")
    return region1


def basic_info(region1):
    """
    병원에 대한 정보를 만드는 함수.
    :param region1: 사용자의 지역
    :return: 사용자 지역의 병원들에 대한 정보를 가져오는 2가지 인스턴스
    """
    hp_data = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?'
    hp_from_add_url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?'

    hospital_data = Hospital_data(hp_data)
    hospital_pos = Hospital_data_from_pos(hp_from_add_url, region1)
    print('페이지 수:' + str(hospital_pos.page_no))
    print(hospital_pos.show_key())

    return hospital_data, hospital_pos


def get_hp_dict(hospital_pos):
    """
    지역의 모든 병원 dictionary를 만드는 함수
    :param hospital_pos: 지역의 병원들에 대한 정보를 가져오는 인스턴스
    :return: 사용자의 지역내의 병원을 '병원명':'병원ID'로 정리
    """
    hp_dict = hospital_pos.get_name_list_id()
    return hp_dict

def get_ER_phone(hospital_data, hp_dict):
    """
    병원 dictionary에서 각 병원의 응급실 전화번호를 검색
    :param hospital_data: 정보 검색용 인스턴스
    :param hp_dict: 검색할 병원의 dictionary
    :return: 병원:전화번호의 dictionary
    """
    ER_phone = hospital_data.get_ERphone_by_HPID(hp_dict)
    return ER_phone


def get_xy(hospital_data, hp_dict):
    """
    병원 dictionary에서 각 병원의 xy좌표를 검색
    :param hospital_data: 정보 검색용 인스턴스
    :param hp_dict: 검색할 병원의 dictionary
    :return: 병원:xy좌표의 dictionary
    """
    xy = hospital_data.get_xy_by_HPID(hp_dict)
    return xy


def get_Address(hospital_data, hp_dict):
    """

    :param hospital_data:
    :param hp_dict:
    :return: 병원:병원주소
    """
    Address = hospital_data.get_Address_by_HPID(hp_dict)
    return Address


def get_data_hospital(hospital_data, treatment_in, hp_l_in, hp_dict_in):
    """
    병원 dictionary에서 모든 입력한 진료과목들을 토대로 가능한 병원들을 추려냄
    :param hospital_data: 정보 검색용 인스턴스
    :param treatment_in: 입력한 진료과목
    :param hp_l_in: 병원 리스트
    :param hp_dict_in: 병원:병원ID의 dictionary
    :return: 입력한 진료과목을 모두 충족하는 병원 리스트, dictionary
    """
    hp_list = []
    hp_dict = {}
    hospital_data.make_soup_list(hp_dict_in)
    for hp in hp_l_in:
        flag = 1
        for i in treatment_in:
            delete = hospital_data.get_info_by_HPID(treatment_name=i, key=hp)
            if delete:
                flag = 0
                break
        if flag:
            hp_list.append(hp)
            hp_dict.update({hp: hp_dict_in[hp]})
    return hp_list, hp_dict


"""
응급 병원 진료 과목
#출처: NIA_IFT_OpenAPI활용가이드-01.국립중앙의료원정보조회서비스
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


#스스로 test 할 수 있도록 만든 code
if __name__ == '__main__':
    # region1 = get_location()
    region1 = '서울특별시' #임의 지역 설정

    hp_data = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?'
    hp_from_add_url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?'
    treatment_list = ['MKioskTy25']

    hospital_data = Hospital_data(hp_data)

    hospital_pos = Hospital_data_from_pos(hp_from_add_url, region1)
    print('페이지 수:' + str(hospital_pos.page_no))
    print(hospital_pos.show_key())

    hp_dict = get_hp_dict(hospital_pos)
    hp_list = list(hp_dict)
    print(1)
    hp_list, hp_dict = get_data_hospital(hospital_data, treatment_list, hp_list, hp_dict)
    print(hp_list)
    xy = hospital_data.get_xy_by_HPID(hp_dict)
    print(xy)


