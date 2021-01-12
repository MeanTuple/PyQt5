import sys
from computer import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Digcalculator(QMainWindow, Ui_MainWindow):
    # 5个公用变量
    lcdString = ''
    operation = ''
    currentNum = 0
    previousNum = 0
    result = 0

    def __init__(self, parent=None):
        super(Digcalculator, self).__init__()
        # UMainWindow.__init__(self)
        self.setupUi(self)
        self.action()

    def action(self):
         self.pushbutton_0.clicked.connect(self.buttonClicked)
         self.pushbutton_1.clicked.connect(self.buttonClicked)
         self.pushbutton_2.clicked.connect(self.buttonClicked)
         self.pushbutton_3.clicked.connect(self.buttonClicked)
         self.pushbutton_4.clicked.connect(self.buttonClicked)
         self.pushbutton_5.clicked.connect(self.buttonClicked)
         self.pushbutton_6.clicked.connect(self.buttonClicked)
         self.pushbutton_7.clicked.connect(self.buttonClicked)
         self.pushbutton_8.clicked.connect(self.buttonClicked)
         self.pushbutton_9.clicked.connect(self.buttonClicked)

         self.pushbutton_plus.clicked.connect(self.opClicked)
         self.pushbutton_minus.clicked.connect(self.opClicked)
         self.pushbutton_multi.clicked.connect(self.opClicked)
         self.pushbutton_divide.clicked.connect(self.opClicked)
         self.pushbutton_euqal.clicked.connect(self.equalClicked)
         self.pushbutton_clear.clicked.connect(self.clearClicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Digcalculator()
    window.show()
    sys.exit(app.exec_())
    
