import bs4
import requests


class Hospital_data:
    def __init__(self):
        url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getSrsillDissAceptncPosblInfoInqire'
        servicekey = '2fyJgtoIO%2Bfhz6MjSwF42UXNxtrsfyivG721At39C6f2ojwkUxL5cD76MJmUEZvoMKXoedSm5aKmKuMYOqSqWA%3D%3D'
        self.connecturl = url + '?servicekey=' + servicekey
        response = requests.get(url + '?servicekey=' + servicekey)
        response.raise_for_status()
        html = response.text
        self.soup = bs4.BeautifulSoup(html, 'html.parser')
        self.reference = url + '\n' + 'service key = ' + servicekey + '\n' + 'expires:' + '2021.11.10'

    def show_url(self):
        return self.connecturl

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
                Hospitals[name_list[j]] = Hospitals[name_list[j]]+i[j]
        return Hospitals


hospital1 = Hospital_data()
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
dict1 = hospital1.create_dict(list1, info1)
print(dict1)
