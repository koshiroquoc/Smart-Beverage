import mysql.connector
import numpy
# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="@May123456", database="maydinhduong")
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
drinks = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
# tạo đối tượng cursor
cur = myconn.cursor()
try:
    # select dữ liệu từ database
    cur.execute(f"SELECT ID  FROM weekreport WHERE {weekdays[0]}=''")

    # tìm nạp các hàng từ đối tượng con trỏ
    result = cur.fetchall()
    data = numpy.array(result)
    for item in data:
        value = item[0]
        print(value)
        cur = myconn.cursor()
        try:
            query = f"SELECT NAME FROM users WHERE ID=%a"%item[0]
            cur.execute(query)
            myresult = cur.fetchall()
            data2 = numpy.array(myresult)
            for items in data2:
                print(items[0])
        except:
            myconn.rollback()
except:
    myconn.rollback()

print("Layten")
# tạo đối tượng cursor
cur = myconn.cursor()
id=1
try:
    # select dữ liệu từ database
    cur.execute(f"SELECT {weekdays[1]}  FROM weekreport WHERE ID=%a"%id)

    # tìm nạp các hàng từ đối tượng con trỏ
    result = cur.fetchall()
    data = numpy.array(result)
    if data[0][0]!='':
        print(data[0][0])
    else:
        print("chuwa uong")
    for item in data:
        value = item[0]

        print(value)
except:
    myconn.rollback()


myconn.close()