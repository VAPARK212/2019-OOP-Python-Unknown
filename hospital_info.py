import bs4
import requests
import math


class Hospital:
    """
    url을 토대로 원하는 정보를 가져오는 class
    """

    def __init__(self, url):
        self.url = url
        self.servicekey = '2fyJgtoIO%2Bfhz6MjSwF42UXNxtrsfyivG721At39C6f2ojwkUxL5cD76MJmUEZvoMKXoedSm5aKmKuMYOqSqWA%3D%3D'
        self.connecturl = self.url + '&servicekey=' + self.servicekey
        response = requests.get(self.connecturl)
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

    def get_info_by_HPID(self, treatment_name, info, HPID):
        connecturl = self.connecturl + '&HPID=' + HPID
        response = requests.get(connecturl)
        response.raise_for_status()
        html = response.text
        soup4search = bs4.BeautifulSoup(html, 'html.parser')

        info_recv = soup4search.select(treatment_name)
        try:
            info_recv = info_recv[0].getText()
        except IndexError:
            info_recv = 'U'  # U for Unknown
        info.append(info_recv)

    def get_ERphone_by_HPID(self, hp_dict):
        ER_phone = {}
        for hp in hp_dict:
            connecturl = self.connecturl + '&HPID=' + hp_dict[hp]
            response = requests.get(connecturl)
            response.raise_for_status()
            html = response.text
            soup4search = bs4.BeautifulSoup(html, 'html.parser')

            info_recv = soup4search.select('dutyTel3')
            try:
                info_recv = info_recv[0].getText()
            except IndexError:
                info_recv = 'U'  # U for Unknown
            ER_phone.update({hp: info_recv})
        return ER_phone

    def get_Address_by_HPID(self, hp_dict):
        Address = {}
        for hp in hp_dict:
            connecturl = self.connecturl + '&HPID=' + hp_dict[hp]
            response = requests.get(connecturl)
            response.raise_for_status()
            html = response.text
            soup4search = bs4.BeautifulSoup(html, 'html.parser')

            info_recv = soup4search.select('dutyAddr')
            try:
                info_recv = info_recv[0].getText()
            except IndexError:
                info_recv = 'U'  # U for Unknown
            Address.update({hp: info_recv})
        return Address

    def create_dict(self, name_list, infolist):
        Hospitals = {}
        for j in range(len(name_list)):
            Hospitals.update({name_list[j]: ''})
            for data in infolist[j]:
                Hospitals[name_list[j]] = Hospitals[name_list[j]] + data

        return Hospitals


class Hospital_data_from_pos(Hospital):
    """
    Hospital 의 위치를 가지고 hpid 기관 ID, 기관명, 응급실 전번을 가져온다.
    """

    def __init__(self, url, add1):  # Q0 주소(시도) 입력
        self.add1 = add1
        self.url = url + '&Q0=' + self.add1
        self.url_tmp = ''

        super().__init__(self.url)

        page_no_list = self.soup.select('totalCount')
        self.page_no = math.ceil(int(page_no_list[0].getText()) / 10)

    def get_name_list_id(self):
        name_list_id = {}
        for i in range(self.page_no):
            url_tmp = self.url + '&pageNo=' + str(i+1)
            self.connecturl = url_tmp + '&servicekey=' + self.servicekey
            response = requests.get(self.connecturl)
            response.raise_for_status()
            html = response.text
            self.soup = bs4.BeautifulSoup(html, 'html.parser')

            name_list = self.soup.select('dutyName')
            id_list = self.soup.select('hpid')

            for j in range(len(name_list)):
                name_list_id.update({name_list[j].getText(): id_list[j].getText()})
        return name_list_id


    def get_detailAdress(self, name_list):
        Address_list = self.soup.select('dutyAddr')
        Address = {}

        for i in range(len(Address_list)):
            Address.update({name_list[i]: Address_list[i].getText()})

        return Address

