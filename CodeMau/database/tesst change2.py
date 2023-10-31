import mysql.connector
import numpy
# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="@May123456", database="maydinhduong")

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
drinks = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
cur = myconn.cursor()
id=3
try:
    # Cập nhật bảng
    query = f"UPDATE weekreport SET {weekdays[0]} = %s WHERE id = %s"
    values = (drinks[1], 4)
    cur.execute(query, values)

    # Lưu thay đổi
    myconn.commit()

except:
    myconn.rollback()