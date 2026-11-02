# Bài 1 Nhập số nguyên n từ bàn phím
import math


n = int(input("Nhập vào số nguyên n: "))

# Tính số gấp đôi của n
ket_qua = n * 2

# In kết quả ra màn hình
print("Số gấp đôi của n là:", ket_qua)


#Bài 2  Nhập chiều rộng a và chiều dài b (có thể là số thực)
a = float(input("Nhập chiều rộng a: "))
b = float(input("Nhập chiều dài b: "))

# Tính diện tích hình chữ nhật
S_hcn = a * b

# Tính bán kính hình tròn (bằng một nửa chiều rộng)
r = a / 2

# Tính diện tích hình tròn với pi = 3.14
S_tron = 3.14 * (r ** 2)

# Tính diện tích còn lại để trồng cây
S_con_lai = S_hcn - S_tron

# In kết quả làm tròn đến 2 chữ số thập phân
print(f"Diện tích còn lại để trồng cây là: {S_con_lai:.2f}")


#Bài 3  Nhập vào một kí tự c
c = input("Nhập vào một kí tự: ")

# Kiểm tra nếu là chữ hoa thì đổi thành chữ thường
if 'A' <= c <= 'Z':
    print(c.lower())
# Nếu là chữ thường thì đổi thành chữ hoa
elif 'a' <= c <= 'z':
    print(c.upper())
else:
    print("Đây không phải là chữ cái thuộc bảng alphabet.")


# Bài 4 Nhập vào một kí tự c
c = input("Nhập vào một kí tự c: ")

# Kiểm tra xem c có phải chữ cái hay không
if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
    print(f"{c} là ki tu alphabet")
else:
    print(f"{c} khong phai la ki tu alphabet")

#Bài 5  Nhập vào một chữ cái hoa A
A = input("Nhập vào chữ cái hoa: ")

# Xét trường hợp đặc biệt khi c = 'A'
if A == 'A':
    print("z")
else:
    # Chuyển về chữ thường tương ứng
    chu_thuong = A.lower()
    # Lấy kí tự đứng liền trước dựa trên mã ASCII
    lien_truoc = chr(ord(chu_thuong) - 1)
    print(lien_truoc)


#Bài 6 
# import math 

# Nhập vào 3 số a, b, c
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Điều kiện để 3 số tạo thành một tam giác
if (a + b > c) and (a + c > b) and (b + c > a):
    # Tính nửa chu vi
    p = (a + b + c) / 2
    # Tính diện tích theo công thức Heron
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    # In ra kết quả với 1 chữ số thập phân
    print(f"Diện tích tam giác là: {dien_tich:.1f}")
else:
    print("Khong phai 3 canh cua tam giac")


#Bài 7  Nhập vào một chuỗi độ dài >= 20
chuoi = input("Nhập vào một chuỗi (độ dài >= 20): ")

# Kiểm tra độ dài chuỗi để tránh lỗi
if len(chuoi) >= 20:
    # Kí tự thứ 5 (index 4) và thứ 9 (index 8)
    print("Kí tự thứ năm là:", chuoi[4])
    print("Kí tự thứ chín là:", chuoi[8])
else:
    print("Chuỗi nhập vào quá ngắn, độ dài phải >= 20.")


#Bài 8 # 1. Nhập thông tin từ người dùng
ho_ten = input("Nhập họ tên chủ hộ: ")
chi_so_cu = int(input("Nhập chỉ số điện kế tháng trước: "))
chi_so_moi = int(input("Nhập chỉ số điện kế tháng này: "))

# 2. Tính số điện tiêu thụ
so_dien = chi_so_moi - chi_so_cu

if so_dien < 0:
    print("Lỗi: Chỉ số tháng này không thể nhỏ hơn chỉ số tháng trước!")
else:
    tien_dien = 0

    # Bậc 1: Từ 0 đến 50 kWh (Tối đa 50 kWh)
    if so_dien > 50:
        tien_dien += 50 * 1984
        so_dien -= 50
    else:
        tien_dien += so_dien * 1984
        so_dien = 0

    # Bậc 2: Từ 51 đến 100 kWh (Tối đa 50 kWh tiếp theo)
    if so_dien > 50:
        tien_dien += 50 * 2050
        so_dien -= 50
    else:
        tien_dien += so_dien * 2050
        so_dien = 0

    # Bậc 3: Từ 101 đến 200 kWh (Tối đa 100 kWh tiếp theo)
    if so_dien > 100:
        tien_dien += 100 * 2380
        so_dien -= 100
    else:
        tien_dien += so_dien * 2380
        so_dien = 0

    # Bậc 4: Từ 201 đến 300 kWh (Tối đa 100 kWh tiếp theo)
    if so_dien > 100:
        tien_dien += 100 * 2998
        so_dien -= 100
    else:
        tien_dien += so_dien * 2998
        so_dien = 0

    # Bậc 5: Từ 301 đến 400 kWh (Tối đa 100 kWh tiếp theo)
    if so_dien > 100:
        tien_dien += 100 * 3350
        so_dien -= 100
    else:
        tien_dien += so_dien * 3350
        so_dien = 0

    # Bậc 6: Từ 401 kWh trở đi (Toàn bộ số điện còn lại)
    if so_dien > 0:
        tien_dien += so_dien * 3460

    # 3. Xuất kết quả ra màn hình
    print("\n--- HÓA ĐƠN TIỀN ĐIỆN ---")
    print(f"Chủ hộ: {ho_ten}")
    print(f"Tổng tiền điện tháng này phải trả: {tien_dien:,} đồng")




