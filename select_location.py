import sys
from PyQt5.QtWidgets import *

enter_flag=False
text = '?'

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global enter_flag
        self.qle = QLineEdit(self)
        self.qle.move(20, 100)

        enter = QPushButton('Enter',self)
        enter.move(50, 50)
        enter.resize(enter.sizeHint())

        self.setWindowTitle('Location')
        self.setGeometry(300, 300, 1000, 200)
        self.show()
        enter.clicked.connect(self.return_text)
        enter_flag=True

        # enter 버튼을 누르면 그 시그널이 괄호안의 함수로 전달 됩니다.
        # 그 시그널이 눌리면 qle.text 값을 객체 밖으로 리턴 해주고 싶은상황입니다.

    def return_text(self):
        pass_test(self.qle.text())
        # self.qle.text() 전달하도록

    def click_location(self, test_location):

        rbtn = []
        cnt = 0

        for loc in test_location :
            rbtn.append(QRadioButton(loc, self))
            rbtn[cnt].move(50, 50+20*cnt)
            cnt+=1


def pass_test(txt):
    print("??")
    global text
    text = txt

if __name__ == '__main__':

    test_location = ['세종과학예술영재학교 | 세종특별자치시 달빛1로 265',
                     '지진실내구호소 세종과학예술영재학교 | 세종특별자치시 달빛1로 265',
                     '지진옥외대피소 세종과학예술영재학교 운동장 | 세종특별자치시 달빛1로 265']

    dict = {'세종과학예술영재학교' : test_location}

    app = QApplication(sys.argv)
    ex = MyApp()
    while not enter_flag:
        continue
    print(text)
    ex.click_location(dict[text])
    sys.exit(app.exec_())
