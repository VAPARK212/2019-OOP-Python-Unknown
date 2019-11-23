import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import main_example

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

        self.setGeometry(300, 300, 500, 300)
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
    @pyqtSlot()
    def new_page(self):
        '''
        새로운 페이지를 생성.
        최상위 5개 병원에 대한 정보를 출력할 수 있는 공간 제작.
        stk_w (=> QStackedWidget(self)) 를 이용하여 여러 위젯을 겹쳐 띄울 수 있게 됨.
        :return:
        '''
        self.stk_w.addWidget(new_widget())
        self.widget_laytout.addWidget(self.stk_w)
        self.setLayout(self.widget_laytout)


    @pyqtSlot()
    def hospital(self,treat_li):

        print('""')
        print(treat_li)
        print('""')

        # main_example.py와 합작
        # ip 주소를 이용하여 현재 위치 파악
        region = main_example.get_location()
        # 현재 region 안에 있는 병원들의
        self.hospital_data, self.hospital_pos =  main_example.basic_info(region)
        # 현재 region 안에 있는 병원들의
        self.hp_dict = main_example.get_hp_dict(self.hospital_pos)
        self.hp_list = list(self.hp_dict)

        self.treatment_list = []

        for i in range(0, 12):
            if treat_li[i] is 1:
                if i is not 12:
                    self.treatment_list.append('MKioskTy' + '%d' % i)
                else:
                    self.treatment_list.append('MKioskTy12')

        main_example.get_data_hospital(self.hospital_data, self.treatment_list, self.hp_list, self.hp_dict)


class StWidgetForm(QGroupBox):
    '''
    new_widget의 부모 클래스.
    QGroupBox 형식.
    '''
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(self.box)


class new_widget(StWidgetForm):
    '''
    추가로 띄우는 widget.
    QLabel 형식으로 병원 정보 작성하도록 함.
    '''
    def __init__(self,Address, ER_phone):
        super(new_widget, self).__init__()
        self.setTitle("Hospital recommendation")
        self.hosp_info = []
'''
        self.Label(Address, ER_phone)

        self.box.addWidget(QLabel(hosp_info[1])) # 병원 정보 작성.
        self.box.addWidget(QLabel(hosp_info[2]))
        self.box.addWidget(QLabel(hosp_info[3]))
        self.box.addWidget(QLabel(hosp_info[4]))
        self.box.addWidget(QLabel(hosp_info[5]))


    def Label(self, Address, ER_phone):
        for i in range(0,5):
            hos_label = '기관명 : ' +
                           '기관 id : ' +
                           '주소 : ' + Address
                           '응급실 전화 : ' + ER_phone
            hosp_info.append(hos_label)
'''




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())