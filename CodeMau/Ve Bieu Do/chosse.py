import random
import matplotlib.pyplot as plt

# Khởi tạo các giá trị
drink_types = ['Sữa tươi', 'Sữa đậu', 'Nước cam']
no_sugar_values = [0, 0, 0]
low_sugar_values = [0, 0, 0]
high_sugar_values = [0, 0, 0]
total_choices = 50  # Tổng số lần chọn

# Tiến hành lựa chọn đồ uống
for i in range(total_choices):
    choice = random.choice(drink_types)
    if choice == 'Sữa tươi':
        sugar_level = random.choice(['không đường', 'ít đường', 'nhiều đường'])
        if sugar_level == 'không đường':
            no_sugar_values[0] += 1
        elif sugar_level == 'ít đường':
            low_sugar_values[0] += 1
        else:
            high_sugar_values[0] += 1
    elif choice == 'Sữa đậu':
        sugar_level = random.choice(['không đường', 'ít đường', 'nhiều đường'])
        if sugar_level == 'không đường':
            no_sugar_values[1] += 1
        elif sugar_level == 'ít đường':
            low_sugar_values[1] += 1
        else:
            high_sugar_values[1] += 1
    else:
        sugar_level = random.choice(['không đường', 'ít đường', 'nhiều đường'])
        if sugar_level == 'không đường':
            no_sugar_values[2] += 1
        elif sugar_level == 'ít đường':
            low_sugar_values[2] += 1
        else:
            high_sugar_values[2] += 1

# Vẽ biểu đồ
opacity = 0.8  # Độ mờ của các cột
bar_width = 0.25  # Kích thước của các cột

# Chỉ số của các cột
index = [i for i in range(len(drink_types))]
index = [float(i) for i in index]

# Thêm mã cho biểu đồ
ects1 = plt.bar(index, no_sugar_values, bar_width, alpha=opacity, color='b', label='không đường')
ects2 = plt.bar([i + bar_width for i in index], low_sugar_values, bar_width, alpha=opacity, color='g', label='ít đường')
ects3 = plt.bar([i + 2*bar_width for i in index], high_sugar_values, bar_width, alpha=opacity, color='r', label='nhiều đường')

# Đặt nhãn trục x và y, tên biểu đồ, tên nhãn
plt.xlabel('Loại đồ uống')
plt.ylabel('Số lượng')
plt.title('Thống kê đồ uống của 10 bạn học sinh trong 1 tuần')

# Đặt tên cho các nhóm cột
plt.xticks([i + bar_width for i in index], drink_types)

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()

# Tính tổng số đồ uống của mỗi loại






