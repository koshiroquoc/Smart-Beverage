import mysql.connector

# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="123456", database="coffeemachine")

# tạo đối tượng cursor
cur = myconn.cursor()
sql = ("insert into quanly(Name, CS, CD, NC, CR,TCS,TCD,TNC,TCR,Tong) "
       + "values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)")

# giá trị của một row được cung cấp dưới dạng tuple
val = [("quoc", 90, 90,100,100,0,0,0,0,0),
       ("khanh", 68, 95,95,100,0,0,0,0,0),
       ("giang", 93, 90,100,100,0,0,0,0,0),
       ("lan", 90, 95,90,100,0,0,0,0,0),
       ("hoang", 90, 86,100,80,0,0,0,0,0)]

try:
    # inserting the values into the table
    cur.executemany(sql, val)

    # commit the transaction
    myconn.commit()

except:
    myconn.rollback()

print(cur.rowcount, "record inserted!")
myconn.close()