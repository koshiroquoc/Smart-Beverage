import mysql.connector

import telegram
import asyncio

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
        await bot.sendPhoto(chat_id=chat_id, photo=open("total_drinks.png", "rb"), caption="Report")
    print('Message Sent!')

import matplotlib.pyplot as plt
import numpy as np
# tạo đối tượng connection
myconn = mysql.connector.connect(host="localhost", user="root",
                                 passwd="@May123456", database="maydinhduong")
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
drinks = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
types = ['Không đường', 'Ít đường', 'Nhiều đường']
# tạo đối tượng cursor
type1=types[0]
drink=drinks[1]

print("phan 2")
cur = myconn.cursor()
try:
    b=str(drinks.index(drink))+str(types.index(type1))
    sql1 = "SELECT * FROM tongket WHERE TYPE = %s" % b
    cur.execute(sql1)
    myresult1 = cur.fetchall()
    print(myresult1)
    print(myresult1[0][1])
    dass=int(myresult1[0][1])+3
   # print(dass)
except:
    myconn.rollback()

print("Phan 3")
cur = myconn.cursor()
try:
    b=str(drinks.index(drink))+str(types.index(type1))
    sql1 = "SELECT USED FROM tongket"
    cur.execute(sql1)
    lst = cur.fetchall()
    arr = []  # khởi tạo mảng rỗng
    for tpl in lst:
        arr.append(int(tpl[0]))  # chuyển đổi phần tử của tuple sang kiểu int và thêm vào mảng
    #print(arr)
    colors = ['r', 'g', 'b']
    x = np.arange(len(drinks))
    width = 0.3
    fig, ax = plt.subplots()
    b = np.array(arr).reshape(3, 3)
    #print(b)
    rects = []
    for i in range(len(types)):
        rects.append(ax.bar(x + i * width, b[:, i], width, color=colors[i], label=types[i]))
        #print(b[:, i])

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
    plt.savefig("total_drinks.png")
    # asyncio.run(send(MessageString, 6212688305, my_token,1)) # Goes to Selection_Testing

    #plt.show()
except:
    myconn.rollback()

print("phan 4")
# doc mang thong tin hoc sinh theo id
MessageString="Thông tin sử dụng đồ uống trong tuần của học sinh "
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
        MessageString=MessageString + name
        sql1 = "SELECT * FROM weekreport WHERE ID = %d" %i
        cur.execute(sql1)
        myresult1 = cur.fetchall()
        Data=''
        for y in myresult1:
            Data=y
        ngay = 2
        for index, value in enumerate(Data[1:], start=1):
            if value=="":
                value= 'không sử dụng nước'
            MessageString = MessageString + f'\nThứ {ngay}: {value}'
            ngay += 1
        #print(int(phone))
        if phone!='':
            print(name)
            print(phone)
            asyncio.run(send(MessageString, phone, my_token, 1))  # Goes to Selection_Testing
        MessageString = "Thông tin sử dụng đồ uống trong tuần của học sinh "

except:
    myconn.rollback()
#asyncio.run(send(MessageString, 6212688305, my_token,1)) # Goes to Selection_Testing