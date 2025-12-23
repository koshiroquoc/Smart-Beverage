# Hướng dẫn cài đặt & chạy hệ thống Smart-Beverage (ngay22.py)

Tài liệu này dành cho người **không rành kỹ thuật**. Mục tiêu là cài được phần mềm trên máy mới, cắm Arduino và chạy được hệ thống.

> Ghi chú quan trọng: **Số điện thoại trong database chính là Telegram chat ID** của học sinh (để gửi tin). Hãy nhập đúng Telegram ID.

---

## 0) Chuẩn bị trước
Bạn cần chuẩn bị:
- Máy tính Windows (khuyến nghị Windows 10/11).
- Có kết nối Internet.
- Có Arduino + dây USB để cắm vào máy.
- Webcam (hoặc camera USB) để quét mã QR.

---

## 1) Tải mã nguồn từ GitHub
1. Mở trình duyệt và vào GitHub của bạn (chủ project).
2. Vào repository `Smart-Beverage`.
3. Bấm nút **Code** → chọn **Download ZIP**.
4. Giải nén ZIP ra một thư mục dễ nhớ, ví dụ: `D:\Smart-Beverage`.

---

## 2) Cài phần mềm cần thiết
### 2.1. Cài Python
1. Tải Python từ https://www.python.org/downloads/
2. Khi cài, **nhớ tick vào “Add Python to PATH”**.
3. Cài xong, mở **Command Prompt** và gõ:
   ```
   python --version
   ```
   Nếu hiện phiên bản (ví dụ 3.10.x) là OK.

### 2.2. Cài Git (nếu cần dùng git clone)
Nếu bạn **không** tải ZIP thì có thể cài Git:
- Tải từ https://git-scm.com/downloads
- Sau đó chạy lệnh:
  ```
  git clone <link_repo_github>
  ```

### 2.3. Cài MySQL
1. Tải MySQL Community Server: https://dev.mysql.com/downloads/mysql/
2. Cài đặt, đặt password cho user `root`.
3. **Mật khẩu mặc định trong code đang là `@May123456`**.
   - Nếu đặt mật khẩu khác, phải sửa lại trong file `ngay22.py`.

### 2.4. Cài Arduino IDE
1. Tải Arduino IDE: https://www.arduino.cc/en/software
2. Cài đặt bình thường.

### 2.5. Cài VLC Player
Một số file dùng `python-vlc`, nên cần cài VLC:
- Tải và cài VLC: https://www.videolan.org/vlc/

---

## 3) Cài thư viện Python
Mở **Command Prompt** rồi chạy các lệnh sau:

```
pip install PyQt5 opencv-python numpy matplotlib python-vlc pygame playsound pyserial mysql-connector-python python-telegram-bot
```

Nếu lỗi `pip`, thử:
```
python -m pip install PyQt5 opencv-python numpy matplotlib python-vlc pygame playsound pyserial mysql-connector-python python-telegram-bot
```

---

## 4) Tạo database MySQL
Trong thư mục project có file SQL sẵn:
```
database\maydinhduong_schema.sql
```

### Cách import:
1. Mở **Command Prompt**.
2. Chuyển tới thư mục project, ví dụ:
   ```
   cd D:\Smart-Beverage
   ```
3. Chạy lệnh (thay `PASSWORD` bằng mật khẩu MySQL root của bạn):
   ```
   mysql -u root -pPASSWORD < database\maydinhduong_schema.sql
   ```

Sau khi chạy xong, MySQL sẽ có database `maydinhduong` và các bảng cần thiết.

---

## 5) Nạp code Arduino
1. Mở Arduino IDE.
2. Mở file:
   ```
   Arduino\MDD15032023.ino
   ```
   (hoặc `MDD15032023\MDD15032023.ino` nếu file kia không chạy).
3. Cắm Arduino vào máy tính bằng USB.
4. Trong Arduino IDE, chọn đúng **Board** và **COM Port**.
5. Bấm **Upload** để nạp chương trình.

---

## 6) Chỉnh cấu hình trong `ngay22.py`
Mở file `ngay22.py` bằng Notepad hoặc VSCode.

### 6.1. Chỉnh MySQL password
Tìm đoạn:
```python
mysql.connector.connect(host="localhost", user="root", passwd="@May123456", database="maydinhduong")
```
Nếu mật khẩu MySQL khác, sửa `@May123456` thành mật khẩu bạn đã cài.

### 6.2. Chỉnh cổng COM của Arduino
Tìm đoạn:
```python
arduino = serial.Serial('COM3', 115200)
```
Nếu máy bạn là `COM4` hoặc khác, sửa lại đúng cổng.

Bạn có thể xem COM trong **Device Manager** → mục **Ports (COM & LPT)**.

---

## 7) Chuẩn bị dữ liệu mẫu trong MySQL
Bạn cần nhập dữ liệu học sinh vào bảng `users` và `weekreport`.

Ví dụ (chỉ là mẫu):
```sql
INSERT INTO users (ID, NAME, PHONE, STATUS, VAR, HEALTH)
VALUES (1, 'Nguyen Van A', '123456789', 0, 150, 1);

INSERT INTO weekreport (ID) VALUES (1);
```

**Quan trọng:** `PHONE` chính là **Telegram chat ID** của học sinh.

---

## 8) Chạy chương trình
1. Mở **Command Prompt**.
2. Vào thư mục project:
   ```
   cd D:\Smart-Beverage
   ```
3. Chạy:
   ```
   python ngay22.py
   ```

Nếu chạy đúng, giao diện sẽ hiện lên và bắt đầu quét QR.

---

## 9) Kiểm tra hoạt động
- Quét QR học sinh → UI hiển thị thông tin.
- Chọn đồ uống → hệ thống gửi lệnh qua Arduino.
- Arduino nhận lệnh → máy pha đồ uống chạy.
- Thông tin sẽ ghi vào database + gửi Telegram report (nếu đủ điều kiện).

---

## 10) Lỗi thường gặp & cách xử lý
### 10.1. Lỗi MySQL Access Denied
- Sai password hoặc MySQL chưa chạy.
- Sửa lại password trong `ngay22.py`.

### 10.2. Không thấy COM Port
- Arduino chưa cắm hoặc chưa cài driver.
- Kiểm tra lại Device Manager.

### 10.3. Lỗi không mở được camera
- Đảm bảo webcam đã cắm.
- Nếu máy có nhiều camera, có thể thử đổi `cv2.VideoCapture(0)` thành `cv2.VideoCapture(1)`.

---

## 11) File quan trọng trong project
- `ngay22.py` → file chạy chính.
- `main_page.ui` + `select_ui.ui` → giao diện.
- `audio/` → âm thanh.
- `Arduino/MDD15032023.ino` → firmware Arduino.
- `database/maydinhduong_schema.sql` → script tạo DB.

---

Nếu cần, bạn có thể nhắn lại để bổ sung schema chi tiết hoặc hỗ trợ debug online.
