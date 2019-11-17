import bs4
import requests


class Hospital:
    """
    url을 토대로 원하는 정보를 가져오는 class
    """

    def __init__(self, url):
        self.url = url
        self.servicekey = '2fyJgtoIO%2Bfhz6MjSwF42UXNxtrsfyivG721At39C6f2ojwkUxL5cD76MJmUEZvoMKXoedSm5aKmKuMYOqSqWA%3D%3D'
        self.connecturl = self.url + '&servicekey=' + self.servicekey
        response = requests.get(self.url + '&servicekey=' + self.servicekey)
        response.raise_for_status()
        html = response.text
        self.soup = bs4.BeautifulSoup(html, 'html.parser')
        self.reference = self.url + '\n' + 'service key = ' + self.servicekey + '\n' + 'expires:' + '2021.11.10'

    def show_url(self):
        return self.connecturl

    def show_key(self):
        return self.reference


class Hospital_data(Hospital):
    """
    parsing으로 data를 가져온다
    """

    def __init__(self, url):
        super().__init__(url)

    def get_name_list(self):
        name_list = self.soup.select('dutyName')
        for i in name_list:
            name_list[name_list.index(i)] = i.getText()
        return name_list

    def get_info(self, treatment_name, info):
        infolist = self.soup.select(treatment_name)
        for j in infolist:
            tmp = j.getText()
            infolist[infolist.index(j)] = tmp
        info.append(infolist)

    def create_dict(self, name_list, infolist):
        Hospitals = {}
        for j in range(len(name_list)):
            Hospitals.update({name_list[j]: ''})
            for i in infolist:
                Hospitals[name_list[j]] = Hospitals[name_list[j]] + i[j]
        return Hospitals


class Hospital_data_from_pos(Hospital_data):
    """
    Hospital 의 위치를 가지고 hpid 기관 ID, 기관명, 응급실 전번을 가져온다.
    """

    def __init__(self, url, add1, add2):  # Q0 주소(시도) 입력
        self.add1 = add1
        self.add2 = add2
        self.url = url + '&Q0=' + self.add1 + '&Q1=' + self.add2
        super().__init__(self.url)

    def get_name_list(self):
        name_list = self.soup.select('dutyName')
        for i in name_list:
            name_list[name_list.index(i)] = i.getText()
        return name_list


url1 = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getSrsillDissAceptncPosblInfoInqire?'
hospital_from_add_url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire?'

hospital1 = Hospital_data(url1)
hospital2 = Hospital_data_from_pos(hospital_from_add_url, '서울특별시', '종로구')

print(hospital2.show_url())
list2 = hospital2.get_name_list()
print(list2)

list1 = hospital1.get_name_list()
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
info1 = []
for i in treatment_list:
    hospital1.get_info(treatment_name=i, info=info1)
print(info1)
dict1 = hospital1.create_dict(list2, info1)
print(dict1)
