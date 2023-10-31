import mysql.connector

# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="123456", database="coffeemachine")

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
print("chon 1")
cur = myconn.cursor()
try:
    # select dữ liệu từ database
    sql = "SELECT ID FROM weekreport WHERE Name = 'giang'"

    cur.execute(sql)

    myresult = cur.fetchall()
    print(myresult)


except:
    myconn.rollback()

myconn.close()