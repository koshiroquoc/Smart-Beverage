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

# In ra thông tin về việc uống đồ của học sinh 5 trong tuần
print('Thông tin về việc uống đồ của học sinh 5 trong tuần:')
for day, drink_count in drink_counts.items():
    drink = drink_count['Học sinh 5']
    print(f'{day}: {drink}')

# Vẽ biểu đồ thống kê
drink_counts_student5 = {drink: 0 for drink in drinks}
for drink_count in drink_counts.values():
    drink_counts_student5[drink_count['Học sinh 5']] += 1

plt.bar(drink_counts_student5.keys(), drink_counts_student5.values())
plt.title('Thống kê loại đồ uống của học sinh 5 trong tuần')
plt.xlabel('Loại đồ uống')
plt.ylabel('Tổng số lần uống')
plt.yticks(range(max(drink_counts_student5.values()) + 1))

plt.savefig('drink_counts_student5.png')
plt.show()
