import random
import matplotlib.pyplot as plt

# Tạo danh sách các loại đồ uống
drinks = ['SKĐ', 'SIĐ', 'SNĐ', 'ĐKĐ', 'ĐIĐ', 'ĐNĐ', 'CKĐ', 'CIĐ', 'CNĐ']

# Tạo danh sách các học sinh
students = ['Học sinh ' + str(i) for i in range(1, 11)]

# Tạo dictionary để lưu trữ thông tin về việc uống đồ của các học sinh trong tuần
drink_counts = {'Thứ 2': {}, 'Thứ 3': {}, 'Thứ 4': {}, 'Thứ 5': {}, 'Thứ 6': {}}

# Lặp qua các ngày trong tuần từ thứ 2 đến thứ 6
for day in drink_counts.keys():
    # Lặp qua từng học sinh
    for student in students:
        # Lựa chọn ngẫu nhiên một loại đồ uống cho học sinh
        drink = random.choice(drinks)
        # Lưu thông tin về việc uống đồ của học sinh trong ngày vào dictionary
        drink_counts[day][student] = drink

# In ra thông tin về việc uống đồ của các học sinh trong tuần
for day, drink_count in drink_counts.items():
    print(f'Ngày {day}:')
    for student, drink in drink_count.items():
        print(f'{student} uống {drink}')

# Vẽ biểu đồ thống kê
drink_totals = {drink: 0 for drink in drinks}
for drink_count in drink_counts.values():
    for drink in drink_count.values():
        drink_totals[drink] += 1

plt.bar(drink_totals.keys(), drink_totals.values())
plt.title('Thống kê loại đồ uống trong tuần')
plt.xlabel('Loại đồ uống')
plt.ylabel('Tổng số lần uống')
plt.savefig('drink_totals.png')
plt.show()
