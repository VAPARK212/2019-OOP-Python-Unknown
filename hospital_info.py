import bs4
import requests

class Hospital_data:
    def __init__(self):
        url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getSrsillDissAceptncPosblInfoInqire'
        servicekey = '2fyJgtoIO%2Bfhz6MjSwF42UXNxtrsfyivG721At39C6f2ojwkUxL5cD76MJmUEZvoMKXoedSm5aKmKuMYOqSqWA%3D%3D'
        self.connecturl = url+'?servicekey='+servicekey
        response = requests.get(url + '?servicekey=' + servicekey)
        response.raise_for_status()
        html = response.text
        self.soup = bs4.BeautifulSoup(html, 'html.parser')

    def show_url(self):
        return self.connecturl

    def get_name_list(self):
        name_list = self.soup.select('dutyName')
        for i in name_list:
            name_list[name_list.index(i)] = i.getText()
        return name_list

    def get_info(self):
        infolist = self.soup.select('MKioskTy1')
        for i in infolist:
            tmp = i.getText()
            if tmp == 'Y':
                infolist[infolist.index(i)] = 1
            else:
                infolist[infolist.index(i)] = 0
        return infolist

    def create_dict(self, name_list, infolist):
        Hostpitals= {}
        for hospital in name_list:
            Hostpitals[hospital] = infolist[name_list.index(hospital)]

        return Hostpitals



hospital1 = Hospital_data()
list1 = hospital1.get_name_list()
info1 = hospital1.get_info()
dict1 = hospital1.create_dict(list1, info1)
print(dict1)