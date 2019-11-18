import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import main_example


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.type_of_treatment = ['뇌출혈 수술', '뇌경색의 재관류', '심근경색의 재관류',
                             '복부 손상의 수술', '사지 접합의 수술', '응급 내시경', '응급 투석',
                             '조산 산모', '정신 질환자', '신생아', '중증 화상', '응급실']

        self.treatment = [0,0,0,0,0,0,0,0,0,0,0,0]

        self.stk_w = QStackedWidget(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Emergency')
        self.widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)

        self.widget_laytout.addWidget(self.initGroup())
        self.setLayout(self.widget_laytout)

        self.setGeometry(300, 300, 500, 300)
        self.resize(1000,500)
        self.show()


    def initGroup(self):
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
        self.cb.append(QCheckBox(self.type_of_treatment[i], self))

        self.cb[i].clicked.connect( lambda state, button = i: self.treat(button))


    def initbtn(self):
        self.btn = QPushButton('Enter', self)

        self.btn.clicked.connect(self.new_page)
        self.btn.clicked.connect(lambda state, treat_li = self.treatment : hospital(treat_li))


    @pyqtSlot()
    def treat(self,button):
        if self.cb[button].isChecked() is True:
            self.treatment[button]=1
        else:
            self.treatment[button]=0


    @pyqtSlot()
    def new_page(self):
        self.stk_w.addWidget(new_widget())
        self.widget_laytout.addWidget(self.stk_w)
        self.setLayout(self.widget_laytout)


class StWidgetForm(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(self.box)


class new_widget(StWidgetForm):
    def __init__(self):
        super(new_widget, self).__init__()
        self.setTitle("Hospital recommendation")
        self.box.addWidget(QLabel("Test Label1")) # 병원 정보 작성.
        self.box.addWidget(QLabel("Test Label2"))
        self.box.addWidget(QLabel("Test Label3"))
        self.box.addWidget(QLabel("Test Label4"))
        self.box.addWidget(QLabel("Test Label5"))

def hospital(treat_li):
    treatment_list = []

    for i in range(0,12):
        if treat_li[i] is 1:
            if i is not 12:
                treatment_list.append('MKioskTy' + '%d' % i)
            else:
                treatment_list.append('MKioskTy12')



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())