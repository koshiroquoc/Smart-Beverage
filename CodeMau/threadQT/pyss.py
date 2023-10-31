import sys
# pip install pyqt5, pip install pyqt5 tools
from PyQt5.QtWidgets import QApplication, QMainWindow
# just change the name
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
import time

from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.thread = {}

        self.uic.Button_start_1.clicked.connect(self.start_worker_1)
        self.uic.Button_start_2.clicked.connect(self.start_worker_2)

        self.uic.Button_stop_1.clicked.connect(self.stop_worker_1)
        self.uic.Button_stop_2.clicked.connect(self.stop_worker_2)

    def start_worker_1(self):
        self.thread[1] = ThreadClass(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.my_function)
        self.uic.Button_start_1.setEnabled(False)
        self.uic.Button_stop_1.setEnabled(True)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(index=2)
        self.thread[2].start()
        self.thread[2].signal.connect(self.my_function)
        self.uic.Button_start_2.setEnabled(False)
        self.uic.Button_stop_2.setEnabled(True)

    def stop_worker_1(self):
        self.thread[1].stop()
        self.uic.Button_stop_1.setEnabled(False)
        self.uic.Button_start_1.setEnabled(True)

    def stop_worker_2(self):
        self.thread[2].stop()
        self.uic.Button_stop_2.setEnabled(False)
        self.uic.Button_start_2.setEnabled(True)

    def my_function(self, counter):
        m = counter
        i = self.sender().index

        if i == 1:
            self.uic.lcdNumber_1.display(m)
        if i == 2:
            self.uic.lcdNumber_2.display(m)

class ThreadClass(QtCore.QThread):
    signal = pyqtSignal(int)

    def __init__(self, index=0):
        super().__init__()
        self.index = index

    def run(self):
        print('Starting thread...', self.index)
        counter = 0
        while True:
            counter += 1
            print(counter)
            time.sleep(1)
            if counter == 5:
                counter = 0
            self.signal.emit(counter)

    def stop(self):
        print('Stopping thread...', self.index)
        self.terminate()

if _name_ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())