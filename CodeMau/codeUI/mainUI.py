import os

from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import cv2
import numpy as np
import main_page
#from thongbao import Ui_Form2
import threading
import serial
class capture_video(QThread):
    signal = pyqtSignal(np.ndarray)
    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(capture_video, self).__init__()
    def run(self):

        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            isSuccess, frame = cap.read()
            self.signal.emit(frame)
            key = cv2.waitKey(1)
        cap.release()
        cv2.destroyAllWindows()
    def stop(self):
        print("stop threading", self.index)
        self.terminate()

class UI(QtWidgets.QMainWindow, main_page.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)
        self.tbs = QtWidgets.QMainWindow()
        #self.uic3 = Ui_Form2()
        #self.uic3.setupUi(self.tbs)
        # setting style sheet
        #self.arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
        self.thread = {}
        self.thread[1] = capture_video(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_wecam)
    def show_wecam(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.lb_camera.setPixmap(qt_img)
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
def main():
    app = QApplication(sys.argv)
    form = UI()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
