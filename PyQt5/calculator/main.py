import sys
from calculator import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class Digcalculator(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # super(Digcalculator, self).__init__()
        UMainWindow.__init__(self)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Digcalculator()
    window.show()
    sys.exit(app.exec_())
    