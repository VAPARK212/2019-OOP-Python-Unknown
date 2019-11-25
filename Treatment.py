import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import main_example
from threading import Thread

# 출처: https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        #사용자가 고를 수 있는 선택지 12개
        self.type_of_treatment = ['뇌출혈 수술', '뇌경색의 재관류', '심근경색의 재관류',
                             '복부 손상의 수술', '사지 접합의 수술', '응급 내시경', '응급 투석',
                             '조산 산모', '정신 질환자', '신생아', '중증 화상', '응급실']

        self.treatment = [0,0,0,0,0,0,0,0,0,0,0,0] # 고객이 선택한 선택지 목록

        self.stk_w = QStackedWidget(self) #
        self.initUI() # 최초 창 띄우기

    def initUI(self):
        '''
        최초로 띄우는 창.
        widget_laytout을 만들어 첫번째 그룹을 넣음.
        첫번째 그룹은 받고자 하는 수술을 선택하는 칸.
        :return:
        '''
        self.setWindowTitle('Emergency')
        self.widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)

        self.widget_laytout.addWidget(self.initGroup())
        self.setLayout(self.widget_laytout)

        self.setGeometry(100, 100, 500, 300)
        self.resize(1000,500)
        self.show()


    def initGroup(self):
        '''
        첫번째 그룹. 받고자 하는 수술을 객관식으로 선택하는 그룹.
        12개 항목을 띄움.
        :return:
        '''
        group = QGroupBox("Treatments")

        self.cb = []
        for i in range(0, 12):
            self.initcb(i)

        self.initbtn()

        vbox = QVBoxLayout()
        for i in range(0,12):
            vbox.addWidget(self.cb[i])
        vbox.addWidget(self.btn)
        group.setLayout(vbox)

        return group


    def initcb(self,i):
        '''
        i번째 선택지에 해당하는 체크박스 생성
        체크박스가 선택될 경우 버튼 번호 i와 함께 시그널이 전송됨.
        :param i:
        :return:
        '''
        self.cb.append(QCheckBox(self.type_of_treatment[i], self))

        self.cb[i].clicked.connect( lambda state, button = i: self.treat(button))


    def initbtn(self):
        '''
        Enter 버튼에 해당하는 푸쉬버튼 생성
        푸쉬버튼이 선택될 경우
        객관식 선택 결과를 담은 리스트 treatment와 함게 시그널이 전송됨
          *새로운 창 띄우기는 병원이 최종 결정된 후에 진행해야함.
        :return:
        '''
        self.btn = QPushButton('Enter', self)

        self.btn.clicked.connect(lambda state, treat_li=self.treatment: self.hospital(treat_li))

        # self.btn.clicked.connect(self.new_page)


    @pyqtSlot()
    def treat(self,button):
        '''
        객관식 체크박스 클릭 시 시그널을 받아서 실행되는 슬롯.
        self.treatment[] 리스트에 고객이 원하는 선택지만 1로 최종 저장되도록 작동.
        :param button:
        :return:
        '''
        if self.cb[button].isChecked() is True:
            self.treatment[button]=1
        else:
            self.treatment[button]=0


# Slot이 아니게 될 예정. 병원이 결정되면 실행되도록 할 것.
    def new_page(self,hospital_data, hp_list, hp_dict):
        '''
        새로운 페이지를 생성.
        최상위 5개 병원에 대한 정보를 출력할 수 있는 공간 제작.
        stk_w (=> QStackedWidget(self)) 를 이용하여 여러 위젯을 겹쳐 띄울 수 있게 됨.
        :return:
        '''
        self.stk_w.addWidget(new_widget(hospital_data, hp_list, hp_dict))
        print(1)
        self.widget_laytout.addWidget(self.stk_w)
        print(2)
        self.setLayout(self.widget_laytout)
        print(3)
        self.show()
        print(4)


    @pyqtSlot()
    def hospital(self,treat_li):

        print('""')
        print(treat_li)
        print('""')

        treatment_list = []

        for i in range(0, 12):
            if treat_li[i] is 1:
                if i is not 12:
                    treatment_list.append('MKioskTy' + '%d' % i)
                else:
                    treatment_list.append('MKioskTy12')

        region1 = main_example.get_location()

        hospital_data, hospital_pos = main_example.basic_info(region1)

        hp_dict = main_example.get_hp_dict(hospital_pos)
        hp_list = list(hp_dict)
        print(hp_list)
        print(hp_dict)

        # xy좌표를 불러오는 thread 시간 단축 (48%)
        thread_xy = ThreadWithReturnValue(target=main_example.get_xy, args=(hospital_data, hp_dict))
        thread_xy.start()

        # 전화번호를 불러오는 thread 시간 단축 (48%)
        thread_ER = ThreadWithReturnValue(target=main_example.get_ER_phone, args=(hospital_data, hp_dict))
        thread_ER.start()

        # 주소를 불러오는 thread 시간 단축 (48%)
        thread_Address = ThreadWithReturnValue(target=main_example.get_Address, args=(hospital_data, hp_dict))
        thread_Address.start()


        hp_list, hp_dict = main_example.get_data_hospital(hospital_data, treatment_list, hp_list, hp_dict)
        print(hp_list)
        print(hp_dict)

        #print(main_example.get_ER_phone(hospital_data, hp_dict))

        ## hp_dict 거리 순 정렬 결과 : list.

        for key in hp_dict:
            if key not in hp_list:
                del hp_dict[key]

        print(hp_dict)
        print(hp_list)

        # 앞에서 실행한 thread의 결과를 각각 불러온다. 반환하는 thread 형식
        xy = thread_xy.join()
        print(xy)

        ER_phone = thread_ER.join()
        print(ER_phone)

        Address = thread_Address.join()
        print(Address)

        self.new_page(hospital_data, hp_list, hp_dict)

class StWidgetForm(QGroupBox):
    '''
    new_widget의 부모 클래스.
    QGroupBox 형식.
    '''
    def __init__(self,hospital_data, hp_list, hp_dict):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(self.box)


class new_widget(StWidgetForm):
    '''
    추가로 띄우는 widget.
    QLabel 형식으로 병원 정보 작성하도록 함.
    '''
    def __init__(self,hospital_data, hp_list, hp_dict):

        print('please')
        super(new_widget, self).__init__()
        self.setTitle("Hospital recommendation")
        self.hosp_info = {}

        print(1)
        self.Label(hospital_data, hp_list, hp_dict)

        i = 1
        for _ in hp_list:
            self.box.addWidget(QLabel(self.hosp_info[hp_list[i]]))  # 병원 정보 작성.
            i += 1


    def Label(self,hospital_data, hp_list, hp_dict):

        Address = main_example.get_Address(hospital_data, hp_dict)
        Phone = main_example.get_ER_phone(hospital_data, hp_dict)

        for key in hp_list:
            hos_label = '기관명 : ' + key + '\n' + \
                        '주소 : ' + Address[key] + '\n' +\
                        '응급실 전화 : ' +  Phone[key]

            self.hosp_info.update({key : hos_label})


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())