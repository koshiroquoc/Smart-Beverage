import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="123456", database="coffeemachine")

# tạo đối tượng cursor
cur = myconn.cursor()

try:
    # cập nhật name cho bảng Employee
    cur.execute("update quanly set CS = 85 where Name = 'giang'")
    myconn.commit()

except:
    myconn.rollback()

myconn.close()