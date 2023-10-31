# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PAGE_MAIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_tm = QtWidgets.QPushButton(self.centralwidget)
        self.bt_tm.setGeometry(QtCore.QRect(810, 480, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bt_tm.setFont(font)
        self.bt_tm.setObjectName("bt_tm")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 971, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lb_camera = QtWidgets.QLabel(self.frame)
        self.lb_camera.setGeometry(QtCore.QRect(140, 80, 640, 480))
        self.lb_camera.setMaximumSize(QtCore.QSize(640, 480))
        self.lb_camera.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lb_camera.setLineWidth(1)
        self.lb_camera.setText("")
        self.lb_camera.setObjectName("lb_camera")
        self.lb_thongbao = QtWidgets.QLabel(self.frame)
        self.lb_thongbao.setGeometry(QtCore.QRect(20, 10, 811, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lb_thongbao.setFont(font)
        self.lb_thongbao.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_thongbao.setObjectName("lb_thongbao")
        self.bt_st = QtWidgets.QPushButton(self.frame)
        self.bt_st.setGeometry(QtCore.QRect(40, 209, 250, 250))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bt_st.setFont(font)
        self.bt_st.setIconSize(QtCore.QSize(25, 20))
        self.bt_st.setObjectName("bt_st")
        self.bt_sd = QtWidgets.QPushButton(self.frame)
        self.bt_sd.setGeometry(QtCore.QRect(350, 210, 250, 250))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bt_sd.setFont(font)
        self.bt_sd.setObjectName("bt_sd")
        self.bt_nc = QtWidgets.QPushButton(self.frame)
        self.bt_nc.setGeometry(QtCore.QRect(680, 210, 250, 250))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bt_nc.setFont(font)
        self.bt_nc.setObjectName("bt_nc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_tm.setText(_translate("MainWindow", "THÊM MỚI"))
        self.lb_thongbao.setText(_translate("MainWindow", "Máy cung cấp đồ uống dinh dưỡng cho trẻ em"))
        self.bt_st.setText(_translate("MainWindow", "SỮA TƯƠI"))
        self.bt_sd.setText(_translate("MainWindow", "SỮA ĐẬU"))
        self.bt_nc.setText(_translate("MainWindow", "NƯỚC CAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())