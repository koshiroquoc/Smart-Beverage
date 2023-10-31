import random
import matplotlib.pyplot as plt
import numpy as np

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


drinks = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
sizes = ['Không đường', 'Ít đường', 'Nhiều đường']
students = ['Học sinh ' + str(i) for i in range(1, 11)]
data = np.zeros((len(drinks), len(sizes)))
# Tạo danh sách các học sinh
students = ['Học sinh ' + str(i) for i in range(1, 11)]

# Tạo dictionary để lưu trữ thông tin về việc uống đồ của các học sinh trong tuần
drink_counts = {'Thứ 2': {}, 'Thứ 3': {}, 'Thứ 4': {}, 'Thứ 5': {}, 'Thứ 6': {}}
for day in drink_counts.keys():
    for student in students:
        drink = random.choice(drinks)
        #print(drink)
        size = random.choice(sizes)
        index1 = drinks.index(drink)
        index2 = sizes.index(size)
       # s=str(index1)+str(index2)
        #print(s)
        data[index1][index2] += 1
        #print(data)
        drink_counts[day][student] = drink+' '+size
# In ra thông tin về việc uống đồ của học sinh 5 trong tuần
MessageString='Thông tin về việc uống đồ của học sinh 5 trong tuần:'
#print(MessageString)
for day, drink_count in drink_counts.items():
    drink = drink_count['Học sinh 1']
    #print(f'{day}: {drink}')
    MessageString=MessageString+f'\n{day}: {drink} '

print(MessageString)
colors = ['r', 'g', 'b']
x = np.arange(len(drinks))
width = 0.3
fig, ax = plt.subplots()
rects = []
print(data)
for i in range(len(sizes)):
    rects.append(ax.bar(x + i * width, data[:, i], width, color=colors[i], label=sizes[i]))
    print(data[:, i])
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
#asyncio.run(send(MessageString, 6212688305, my_token,1)) # Goes to Selection_Testing

plt.show()
