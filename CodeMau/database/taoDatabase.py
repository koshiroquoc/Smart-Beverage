import mysql.connector

# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="123456")

# tạo đối tượng cursor
cur = myconn.cursor()

try:
    cur.execute("create database quanlyMay")
    dbs = cur.execute("show databases")
except:
    myconn.rollback()
for x in cur:
    print(x)
# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="123456", database="quanlyMay")

# tạo đối tượng cursor
cur = myconn.cursor()
try:
    # tạo bảng Employee gồm 4 cột name, id, salary, và department id
    dbs = cur.execute("create table quanly2(Name varchar(20) not null primary key, "
        + "CS int not null , CD int not null ,NC int not null ,CR int not null ,TCS int not null ,TCD int not null ,TNC int not null ,TCR int not null , "
        + "Tong int not null)")
except:
    myconn.rollback()

myconn.close()