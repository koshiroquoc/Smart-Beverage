import random
import matplotlib.pyplot as plt
from PIL import Image

# Tạo danh sách các loại đồ uống
drinks = ["SKĐ", "SIĐ", "SNĐ", "ĐKĐ", "ĐIĐ", "ĐNĐ", "CKĐ", "CIĐ", "CNĐ"]

# Khởi tạo ma trận đếm số lần mỗi học sinh uống mỗi loại đồ uống
drink_counts = [[0] * len(drinks) for i in range(10)]

# Thực hiện việc lấy ngẫu nhiên thông tin uống của các học sinh trong một tuần
for i in range(5):
    for j in range(10):
        drink_index = random.randint(0, len(drinks) - 1)
        drink_counts[j][drink_index] += 1

# Tính tổng số đồ uống của tất cả các học sinh
total_drinks = [sum(x) for x in zip(*drink_counts)]

# Lấy thông tin uống của học sinh thứ 5
student_5_drinks = drink_counts[4]

# Hiển thị biểu đồ "Drink counts for student 5"
plt.figure()
plt.bar(drinks, student_5_drinks)
plt.title("Drink counts for student 5")
plt.xlabel("Drinks")
plt.ylabel("Counts")
plt.savefig("student_5_drinks.png")

# Hiển thị biểu đồ "Total drink counts"
plt.figure()
plt.bar(drinks, total_drinks)
plt.title("Total drink counts")
plt.xlabel("Drinks")
plt.ylabel("Counts")
plt.savefig("total_drinks.png")

# Hiển thị biểu đ
from PIL import Image

# Hiển thị biểu đồ "Drink counts for student 5"
im_student_5 = Image.open("student_5_drinks.png")
im_student_5.show()

# Hiển thị biểu đồ "Total drink counts"
im_total = Image.open("total_drinks.png")
im_total.show()