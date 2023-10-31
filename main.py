from screeninfo import get_monitors
for m in get_monitors():
    print(str(m))
import mysql.connector
import numpy
# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="@May123456", database="maydinhduong")
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
drinks = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
types = ['Không đường', 'Ít đường', 'Nhiều đường']
# tạo đối tượng cursor
type=types[1]
drink=drinks[1]

cur = myconn.cursor()
try:
    # select dữ liệu từ database
    cur.execute(f"SELECT {drink} FROM drink")
    # tìm nạp các hàng từ đối tượng con trỏ
    result = cur.fetchall()
    for x in result:
        print(x);
except:
    myconn.rollback()

# tạo đối tượng cursor
cur = myconn.cursor()
try:
    # select dữ liệu từ database
    cur.execute("SELECT * FROM weekreport")

    # tìm nạp các hàng từ đối tượng con trỏ
    result = cur.fetchall()

    for x in result:
        print(x);

except:
    myconn.rollback()
#print("chon 1")
cur = myconn.cursor()
try:
    # select dữ liệu từ database
    #sql = "SELECT ID FROM quanly WHERE Name = 'giang'"
    #sql = "SELECT PHONE FROM users WHERE ID = '1'"
    sql = "SELECT NAME FROM users WHERE ID = '1'"
    cur.execute(sql)

    myresult = cur.fetchall()
    #print(myresult)
    data= numpy.array(myresult)
    print(data[0][0])
    if data[0][0] == '6212688305':
        print("okey")
    a=2
    sql1 = "SELECT * FROM weekreport WHERE ID = %d" %a
    cur.execute(sql1)
    myresult1 = cur.fetchall()
    print(myresult1[0][1])

except:
    myconn.rollback()

# tạo đối tượng cursor
cur = myconn.cursor()
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
drinks = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
try:
    query = f"SELECT {weekdays[0]} FROM weekreport"
    #values = (str(drink + ' ' + type), str(student))
    cur.execute(query)
    myconn.commit()

except:
    myconn.rollback()

myconn.close()

