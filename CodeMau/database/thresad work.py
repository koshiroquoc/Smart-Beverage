import threading
import time
exitFlag = 0
class myThread(threading.Thread):
   def __init__(self, idLuong, tenLuong, soLuong):
      threading.Thread.__init__(self)
      self.threadID = idLuong
      self.name = tenLuong
      self.counter = soLuong
   def run(self):
      print("Bat dau luong: " + self.name)
      print_time(self.name, 5, self.counter)
      print ("Ket thuc luong: " + self.name)
def print_time(tenLuong, soLuong, delay):
   while soLuong:
      if exitFlag:
         tenLuong.exit()
      time.sleep(delay)
      print ("{0}: {1}".format(tenLuong, time.ctime(time.time())))
      soLuong -= 1
# Tao luong moi
luong1 = myThread(1, "Luong-1", 1)
luong2 = myThread(2, "Luong-2", 2)
# Bat dau luong moi
luong1.start()
luong2.start()
print("Thoat khoi luong chinh!")