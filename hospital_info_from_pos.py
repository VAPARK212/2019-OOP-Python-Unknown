from hospital_info import *


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
