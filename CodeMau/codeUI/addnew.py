# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 300)
        Form.setMaximumSize(QtCore.QSize(450, 300))
        self.scrollbar_cs = QtWidgets.QScrollBar(Form)
        self.scrollbar_cs.setGeometry(QtCore.QRect(120, 55, 230, 50))
        self.scrollbar_cs.setMinimum(50)
        self.scrollbar_cs.setMaximum(100)
        self.scrollbar_cs.setSliderPosition(90)
        self.scrollbar_cs.setOrientation(QtCore.Qt.Horizontal)
        self.scrollbar_cs.setObjectName("scrollbar_cs")
        self.scrollbar_cd = QtWidgets.QScrollBar(Form)
        self.scrollbar_cd.setGeometry(QtCore.QRect(120, 115, 230, 50))
        self.scrollbar_cd.setMinimum(50)
        self.scrollbar_cd.setMaximum(100)
        self.scrollbar_cd.setSliderPosition(90)
        self.scrollbar_cd.setOrientation(QtCore.Qt.Horizontal)
        self.scrollbar_cd.setObjectName("scrollbar_cd")
        self.scrollbar_nc = QtWidgets.QScrollBar(Form)
        self.scrollbar_nc.setGeometry(QtCore.QRect(120, 175, 230, 50))
        self.scrollbar_nc.setMinimum(50)
        self.scrollbar_nc.setMaximum(100)
        self.scrollbar_nc.setSliderPosition(100)
        self.scrollbar_nc.setOrientation(QtCore.Qt.Horizontal)
        self.scrollbar_nc.setObjectName("scrollbar_nc")
        self.scrollbar_cc = QtWidgets.QScrollBar(Form)
        self.scrollbar_cc.setGeometry(QtCore.QRect(120, 235, 230, 50))
        self.scrollbar_cc.setMinimum(50)
        self.scrollbar_cc.setMaximum(100)
        self.scrollbar_cc.setSliderPosition(100)
        self.scrollbar_cc.setOrientation(QtCore.Qt.Horizontal)
        self.scrollbar_cc.setObjectName("scrollbar_cc")
        self.lb_scroll_cs = QtWidgets.QLabel(Form)
        self.lb_scroll_cs.setGeometry(QtCore.QRect(360, 65, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_cs.setFont(font)
        self.lb_scroll_cs.setObjectName("lb_scroll_cs")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 65, 31, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lb_scroll_cd = QtWidgets.QLabel(Form)
        self.lb_scroll_cd.setGeometry(QtCore.QRect(360, 125, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_cd.setFont(font)
        self.lb_scroll_cd.setObjectName("lb_scroll_cd")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 125, 31, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lb_scroll_nc = QtWidgets.QLabel(Form)
        self.lb_scroll_nc.setGeometry(QtCore.QRect(360, 185, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_nc.setFont(font)
        self.lb_scroll_nc.setObjectName("lb_scroll_nc")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(400, 185, 31, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lb_scroll_cc = QtWidgets.QLabel(Form)
        self.lb_scroll_cc.setGeometry(QtCore.QRect(360, 245, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_cc.setFont(font)
        self.lb_scroll_cc.setObjectName("lb_scroll_cc")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 245, 31, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lb_scroll_5 = QtWidgets.QLabel(Form)
        self.lb_scroll_5.setGeometry(QtCore.QRect(10, 65, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_5.setFont(font)
        self.lb_scroll_5.setObjectName("lb_scroll_5")
        self.lb_scroll_6 = QtWidgets.QLabel(Form)
        self.lb_scroll_6.setGeometry(QtCore.QRect(10, 125, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_6.setFont(font)
        self.lb_scroll_6.setObjectName("lb_scroll_6")
        self.lb_scroll_7 = QtWidgets.QLabel(Form)
        self.lb_scroll_7.setGeometry(QtCore.QRect(10, 185, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_7.setFont(font)
        self.lb_scroll_7.setObjectName("lb_scroll_7")
        self.lb_scroll_8 = QtWidgets.QLabel(Form)
        self.lb_scroll_8.setGeometry(QtCore.QRect(10, 245, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_8.setFont(font)
        self.lb_scroll_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lb_scroll_8.setObjectName("lb_scroll_8")
        self.lb_scroll_9 = QtWidgets.QLabel(Form)
        self.lb_scroll_9.setGeometry(QtCore.QRect(20, 10, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lb_scroll_9.setFont(font)
        self.lb_scroll_9.setObjectName("lb_scroll_9")
        self.bt_OK2 = QtWidgets.QPushButton(Form)
        self.bt_OK2.setGeometry(QtCore.QRect(320, 10, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_OK2.setFont(font)
        self.bt_OK2.setObjectName("bt_OK2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_scroll_cs.setText(_translate("Form", "90"))
        self.label_2.setText(_translate("Form", "%"))
        self.lb_scroll_cd.setText(_translate("Form", "90"))
        self.label_3.setText(_translate("Form", "%"))
        self.lb_scroll_nc.setText(_translate("Form", "100"))
        self.label_4.setText(_translate("Form", "%"))
        self.lb_scroll_cc.setText(_translate("Form", "100"))
        self.label_5.setText(_translate("Form", "%"))
        self.lb_scroll_5.setText(_translate("Form", "Coffee sữa"))
        self.lb_scroll_6.setText(_translate("Form", "Coffee đen"))
        self.lb_scroll_7.setText(_translate("Form", "Nước Cam"))
        self.lb_scroll_8.setText(_translate("Form", "Cà rốt"))
        self.lb_scroll_9.setText(_translate("Form", "Tên: "))
        self.bt_OK2.setText(_translate("Form", "OK"))
