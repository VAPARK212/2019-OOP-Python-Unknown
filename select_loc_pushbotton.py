import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        test_location = ['세종과학예술영재학교 | 세종특별자치시 달빛1로 265',
                         '지진실내구호소 세종과학예술영재학교 | 세종특별자치시 달빛1로 265',
                         '지진옥외대피소 세종과학예술영재학교 운동장 | 세종특별자치시 달빛1로 265']

        rbtn = []
        cnt = 0

        for loc in test_location :
            rbtn.append(QRadioButton(loc, self))
            rbtn[cnt].move(50, 50+20*cnt)
            cnt+=1

        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 1000, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())