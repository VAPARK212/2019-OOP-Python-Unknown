import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

type_of_treatment = ['뇌출혈 수술', '뇌경색의 재관류', '심근경색의 재관류',
                    '복부 손상의 수술', '사지 접합의 수술', '응급 내시경', '응급 투석',
                    '조산 산모', '정신 질환자', '신생아', '중증 화상']

cb = []
treatment = [0,0,0,0,0,0,0,0,0,0,0]


def initcb(i,self):
    cb.append(QCheckBox(type_of_treatment[i], self))
    cb[i].move(20, 20+20*i)

    # cb[i].toggle()
    # 수정이 필요한 부분
    # cb[i].stateChanged.connect(self.changeTitle)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        for i in range(0,11):
            initcb(i,self)

        for i in range(0,11):
            if cb[i].clicked:
                treatment[i]=cb[i].checkState()

        self.btn = QPushButton('Enter', self)
        self.btn.move(20,240)

        self.setWindowTitle('Emergency')
        self.setGeometry(500, 300, 500, 300)
        self.show()


        self.btn.clicked.connect(self.new)

    def new(self):
        for i in range(0, 11):
            if treatment[i]:
                print(type_of_treatment[i])
        self.setWindowTitle('Treatment')
        self.setGeometry(500, 300, 500, 300)
        self.show()


    '''
    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
    '''

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())