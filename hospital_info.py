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

    def get_name_list(self):
        name_list = self.soup.select('dutyName')
        for i in name_list:
            name_list[name_list.index(i)] = i.getText()
        return name_list

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

    def create_dict(self, name_list, infolist):
        Hospitals = {}
        for j in range(len(name_list)):
            Hospitals.update({name_list[j]: ''})
            for data in infolist[j]:
                Hospitals[name_list[j]] = Hospitals[name_list[j]] + data

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

    def get_name_list_id(self):
        name_list = self.soup.select('dutyName')
        id_list = self.soup.select('hpid')
        name_list_id = {}

        for i in range(len(name_list)):
            name_list_id.update({name_list[i].getText(): id_list[i].getText()})
        return name_list_id

    def get_ER_phone(self, name_list):
        ER_phone_list = self.soup.select('dutyTel3')
        ER_phone = {}

        for i in range(len(ER_phone_list)):
            ER_phone.update({name_list[i]: ER_phone_list[i].getText()})

        return ER_phone

    def get_detailAdress(self, name_list):
        Address_list = self.soup.select('dutyAddr')
        Address = {}

        for i in range(len(Address_list)):
            Address.update({name_list[i]: Address_list[i].getText()})

        return Address

