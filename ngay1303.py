from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import cv2
import numpy
import main_page
from select_page import Ui_Dialog

import vlc
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
import numpy as np
def Sound(sound):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(sound)
    player.set_media(media)
    player.play()
    time.sleep(0.4)
    duration = player.get_length() / 1000
    time.sleep(duration)
import threading
import os
import telegram
import asyncio
from datetime import datetime
my_token = "6255771559:AAGVvLf8C6RwhYHK82NsuigFVon5p-lTH6Q"

async def send(msg, chat_id, token=my_token,typ=1):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    if typ==1:
        await bot.sendMessage(chat_id=chat_id, text=msg)
    else:
        await bot.sendPhoto(chat_id=chat_id, photo=open("baocaotonghop.png", "rb"), caption="Report")
    print('Message Sent!')
import mysql.connector
# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="@May123456", database="maydinhduong")
cur = myconn.cursor()
# tạo đối tượng cursor

drinks = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
types = ['Không đường', 'Ít đường', 'Nhiều đường']
data = np.zeros((len(drinks), len(types)))
# Tạo danh sách các học sinh

# Tạo dictionary để lưu trữ thông tin về việc uống đồ của các học sinh trong tuần
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
student=0
drink=''
type=''
day=0

dangxuly=0
student_name=''

date_sta="17:10"# thoi gian gui bao cao hoc sinh chua uong
date_str="17:11"# thoi gian gui bao cao tong su dung vaf gui cho phu huynh
#MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
gui_canhbao=0
gui_baocao=0

import threading
import time
exitFlag = 0

import serial

# Thiết lập kết nối với Arduino
arduino = serial.Serial('COM4', 115200)
status=''
class myThread(threading.Thread):
   def __init__(self, idLuong, tenLuong, soLuong):
      threading.Thread.__init__(self)
      self.threadID = idLuong
      self.name = tenLuong
      self.counter = soLuong
   def run(self):

      print("Bat dau luong: " + self.name)
      if(self.threadID==1):
          xulyQR()
      elif (self.threadID==2):
          guibaocao()
      elif (self.threadID==3):
          docarduino()
def docarduino():
    global status
    ls=''
    while True:
        status = arduino.readline().decode().strip()
        if status!=ls:
            print(f'Received data from Arduino: {status}')
            if status=='@':
                Sound(str('./audio' + '/555.mp3'))
            ls=status
def guibaocao():
    global cur, dangxuly, student, student_name, day, weekdays, gui_canhbao, gui_baocao,myconn
    while True:
        dt = datetime.now()
        if dt.isoweekday() < 6:  # kiem tra ngay trong tuan
            report_chuauong = " Danh các bạn chưa sử dụng đồ uống ngày " + dt.strftime('%x')
            if dt.strftime("%H:%M") == date_sta:  # ddung thoi gian
                if gui_canhbao == 0:  # da gui canh bao chua
                    print("gui canh bao")
                    cur = myconn.cursor()
                    try:
                        # select dữ liệu từ database
                        cur.execute(f"SELECT ID  FROM weekreport WHERE {dt.strftime('%A')}=''")
                        # tìm nạp các hàng từ đối tượng con trỏ
                        result = cur.fetchall()
                        # print(result)
                        data = numpy.array(result)
                        for item in data:
                            cur = myconn.cursor()
                            try:
                                query = f"SELECT NAME FROM users WHERE ID=%a" % item[0]
                                cur.execute(query)
                                myresult = cur.fetchall()
                                data2 = numpy.array(myresult)
                                for items in data2:
                                    report_chuauong = report_chuauong + '\n' + items[0]
                                    #print(items[0])
                            except:
                                myconn.rollback()
                    except:
                        myconn.rollback()
                    gui_canhbao = 1
                    print(report_chuauong)
                    asyncio.run(send(report_chuauong, 6212688305, my_token, 1))  # Goes to Selection_Testing
            elif gui_canhbao == 1:
                gui_canhbao = 0
            if dt.strftime("%H:%M") == date_str and dt.strftime('%A') == 'Monday':
                if gui_baocao == 0:
                    print("gui bao cao")
                    cur = myconn.cursor()
                    try:
                        sql1 = "SELECT USED FROM tongket"
                        cur.execute(sql1)
                        lst = cur.fetchall()
                        arr = []  # khởi tạo mảng rỗng
                        for tpl in lst:
                            arr.append(int(tpl[0]))  # chuyển đổi phần tử của tuple sang kiểu int và thêm vào mảng
                        print(arr)
                        colors = ['r', 'g', 'b']
                        x = np.arange(len(drinks))
                        width = 0.3
                        fig, ax = plt.subplots()
                        b = np.array(arr).reshape(3, 3)
                        print(b)
                        rects = []
                        for i in range(len(types)):
                            rects.append(ax.bar(x + i * width, b[:, i], width, color=colors[i], label=types[i]))
                            print(b[:, i])

                        ax.set_xticks(x)
                        ax.set_xticklabels(drinks)
                        ax.legend()

                        for i, rect in enumerate(rects):
                            for j in rect:
                                height = j.get_height()
                                ax.annotate('{:.1%}'.format(height / 50), xy=(j.get_x() + j.get_width() / 2, height),
                                            xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
                        plt.title("Thống kê đồ uống của học sinh trong tuần")
                        plt.xlabel("Loại đồ uống")
                        plt.ylabel("Số lượng")
                        plt.savefig("baocaotonghop.png")
                        asyncio.run(send('bao cao', 6212688305, my_token,2)) # Goes to Selection_Testing#so phone cua quanly
                        #plt.show()
                    except:
                        myconn.rollback()
                    # gui den phu huynh
                    MessageString = "Thông tin sử dụng đồ uống trong tuần của học sinh "
                    cur = myconn.cursor()
                    try:
                        for i in range(11):
                            sql2 = "SELECT PHONE,NAME FROM users WHERE ID = %d" % i
                            cur.execute(sql2)
                            myresult2 = cur.fetchall()
                            phone = ''
                            name = ''
                            for x in myresult2:
                                phone, name = x
                            MessageString = MessageString + name
                            sql1 = "SELECT * FROM weekreport WHERE ID = %d" % i
                            cur.execute(sql1)
                            myresult1 = cur.fetchall()
                            Data = ''
                            for y in myresult1:
                                Data = y
                            ngay = 2
                            for index, value in enumerate(Data[1:], start=1):
                                if value == "":
                                    value = 'không sử dụng nước'
                                MessageString = MessageString + f'\nThứ {ngay}: {value}'
                                ngay += 1
                            # print(int(phone))
                            if phone != '':
                                print(name)
                                print(phone)
                                asyncio.run(send(MessageString, phone, my_token, 1))  # Goes to Selection_Testing
                            MessageString = "Thông tin sử dụng đồ uống trong tuần của học sinh "

                    except:
                        myconn.rollback()
                    gui_baocao = 1
            elif gui_baocao == 1:
                gui_baocao = 0

def xulyQR():
    global cur, dangxuly, student, student_name, day, weekdays, gui_canhbao,gui_baocao,dt
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)
    arucoParams = cv2.aruco.DetectorParameters_create()
    #try:
    #    cap = cv2.VideoCapture(0)
    #   # self.arduino.write(bytes(data_write))
    #    print("hello")
    #except Exception as e:
        #print(f'Something went wrong: {e}')
    cap = cv2.VideoCapture(0)
    send_report = 0
    while cap.isOpened():
        dt = datetime.now()
        ret, img = cap.read()
        h, w, _ = img.shape
        width = 1000
        height = int(width * (h / w))
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        corners, ids, rejected = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
        if len(corners) > 0 and dangxuly == 0:
            ids = ids.flatten()
            for (markerCorner, markerID) in zip(corners, ids):
                student = markerID
                #kiemtra dauong chua
                dauong=1
                cur = myconn.cursor()
                try:
                    print(dt.strftime('%A'))
                    cur.execute(f"SELECT {dt.strftime('%A')}  FROM weekreport WHERE ID=%a" % student)
                    # tìm nạp các hàng từ đối tượng con trỏ
                    result = cur.fetchall()
                    data = numpy.array(result)
                    print(data[0][0])
                    if data[0][0] != '':
                        print("da uoongs")
                        dauong=1
                        Sound(str('./audio' + '/444.mp3'))
                    else:
                        print("chuwa uong")
                        dauong=0
                except:
                    myconn.rollback()
                #####################
                if dauong==0:

                    print("[ID student: {}]".format(student))
                    # get name from ID to print
                    sql = "SELECT NAME FROM users WHERE ID = %d" % (student)
                    cur.execute(sql)
                    myresult = cur.fetchall()
                    student_name = numpy.array(myresult)[0][0]
                    Sound(str('./audio' + '/{}.mp3'.format(str(student))))
                    dangxuly = 1
                    # tạo đối tượng cursor
                    try:
                        sql = "SELECT HEALTH FROM users WHERE ID = %d" % (student)
                        cur.execute(sql)
                        myresult = cur.fetchall()
                        print(myresult)
                        data = numpy.array(myresult)
                        print(data[0][0])
                        if data[0][0] == 1:
                            print("Binhf thuong")
                            Sound(str('./audio' + '/333.mp3'))
                        elif data[0][0] == 2:
                            print("beo phi")
                            Sound(str('./audio' + '/111.mp3'))
                        elif data[0][0] == 3:
                            print("Coi xuong")
                            Sound(str('./audio' + '/222.mp3'))

                    except:
                        myconn.rollback()
        # get current datetime
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
class UI(QtWidgets.QMainWindow, main_page.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)
        self.tbs = QtWidgets.QMainWindow()
        #self.arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
        self.bt_st.clicked.connect(self.suatuoi)
        self.bt_sd.clicked.connect(self.suadau)
        self.bt_nc.clicked.connect(self.nuoccam)
        self.Camera = myThread(1, "Camera", 1)
        self.Guibaocao = myThread(2, "Guibaocao", 2)
        self.docarduino = myThread(3, "docarduino", 3)
        # Bat dau luong moi
        self.Camera.start()
        self.Guibaocao.start()
        self.docarduino.start()

    def timess(self):
        print(1212312312)
    def show_wecam(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.lb_camera.setPixmap(qt_img)
    def suatuoi(self):
        global student_name,drink,drinks
        if dangxuly==1:
            self.suatuoi = QtWidgets.QMainWindow()
            self.uic2 = Ui_Dialog()
            self.uic2.setupUi(self.suatuoi)
            # setting text to the label
            self.uic2.lbl_douong.setText("SỮA TƯƠI")
            self.suatuoi.show()
            self.uic2.bt_ok.clicked.connect(self.ok)
            self.uic2.bt_cancel.clicked.connect(self.cancel)
            self.uic2.scroll_custem.valueChanged.connect(lambda: self.custem())
            self.uic2.lbl_name.setText(student_name)
            drink=drinks[0]
            print("khơi tạo ok")
            print("suatuoi")
    def suadau(self):
        global student_name,drink
        if dangxuly == 1:
            self.suatuoi = QtWidgets.QMainWindow()
            self.uic2 = Ui_Dialog()
            self.uic2.setupUi(self.suatuoi)
            # setting text to the label
            self.uic2.lbl_douong.setText("SỮA ĐẬU")
            self.suatuoi.show()
            self.uic2.bt_ok.clicked.connect(self.ok)
            self.uic2.bt_cancel.clicked.connect(self.cancel)
            self.uic2.scroll_custem.valueChanged.connect(lambda: self.custem())
            drink = drinks[1]
            print("khơi tạo ok")
            print("sua dau")
    def nuoccam(self):
        global student_name,drink
        if dangxuly == 1:
            self.suatuoi = QtWidgets.QMainWindow()
            self.uic2 = Ui_Dialog()
            self.uic2.setupUi(self.suatuoi)
            # setting text to the label
            self.uic2.lbl_douong.setText("NƯỚC CAM")
            self.suatuoi.show()
            self.uic2.bt_ok.clicked.connect(self.ok)
            self.uic2.bt_cancel.clicked.connect(self.cancel)
            self.uic2.scroll_custem.valueChanged.connect(lambda: self.custem())
            drink = drinks[2]
            print("khơi tạo ok")
            print("nuoc cam")
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    def custem(self):
        # getting current value
        self.value = self.uic2.scroll_custem.value()
        self.uic2.lbl_custem.setText(str(self.value))
        if self.value > 5:
            self.uic2.radio_nd.setChecked(True)
        elif self.value>0 and self.value<=5:
            self.uic2.radio_id.setChecked(True)
        else:
            self.uic2.radio_kd.setChecked(True)

    def ok(self):
        global arduino,student,student_name,drink,type,types,myconn,dangxuly
        dt = datetime.now()
        value_s=self.uic2.scroll_custem.value()
        print('day Name:', dt.strftime('%A'))
        if self.uic2.radio_kd.isChecked():
            type=types[0]
        elif self.uic2.radio_id.isChecked():
            type = types[1]
            if(value_s==0):
                value_s = 3
        elif self.uic2.radio_nd.isChecked():
            type = types[2]
            if (value_s == 0):
                value_s = 8
        print(dt.strftime('%A') +'  ')
        print(student_name+' da chon ' +drink+' '+type + ' '+ str(value_s))

        # cho do uong va doi thanh cong
        data_write=''
        if drink==drinks[0]:
            data_write = str('S{0}$\n'.format(value_s))
        elif drink==drinks[1]:
            data_write = str('D{0}$\n'.format(value_s))
        elif drink==drinks[2]:
            data_write = str('C{0}$\n'.format(value_s))
        print(data_write)
        try:
            arduino.write(bytes(data_write, 'utf-8'))
            # self.arduino.write(bytes(data_write))
        except Exception as e:
            print(f'Something went wrong: {e}')
        last_status=''
        while True:
            global status
            print(status)

            if status=='&' or status=='Ket thuc':
                break
        print("da hoan thanh luu data")
        ###############################
        # tạo đối tượng cursor
        cur = myconn.cursor()
        try:
            query = f"UPDATE weekreport SET {dt.strftime('%A')} = %s WHERE id = %s"
            values = (str(drink+' '+type), str(student))
            cur.execute(query, values)
            myconn.commit()
            # doc du lieu tu bang tongket khi loai
            b = str(drinks.index(drink)) + str(types.index(type))
            sql1 = "SELECT * FROM tongket WHERE TYPE = %s" % b
            cur.execute(sql1)
            myresult1 = cur.fetchall()
            print(myresult1[0][1])
            dass = int(myresult1[0][1]) + 1
            #
            query = f"UPDATE tongket SET USED = %s WHERE TYPE = %s"
            values = (str(dass), b)
            cur.execute(query, values)
            myconn.commit()
        except:
            myconn.rollback()
        dangxuly =0
        self.suatuoi.close()

    def cancel(self):
        global dangxuly
        print("huy")
        #dangxuly=0
        self.suatuoi.close()

def main():
    app = QApplication(sys.argv)
    form = UI()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
