# Bài 1 Nhập số nguyên n từ bàn phím
n_chu = input("Nhập số nguyên n: ")
n = int(n_chu)  # Chuyển chữ thành số nguyên

# Tính gấp đôi
ket_qua = n * 2

# In kết quả
print("Số gấp đôi là:", ket_qua)


#Bài 2  Nhập hai cạnh của hình chữ nhật
a_chu = input("Nhập chiều rộng a: ")
b_chu = input("Nhập chiều dài b: ")

a = float(a_chu)  # Chuyển thành số thập phân
b = float(b_chu)

# Tính diện tích hình chữ nhật
S_hcn = a * b

# Tính bán kính hình tròn (bằng nửa chiều rộng a)
r = a / 2

# Tính diện tích hình tròn
S_tron = 3.14 * r * r

# Tính diện tích trồng cây còn lại
S_con_lai = S_hcn - S_tron

# In kết quả, làm tròn lấy 2 số sau dấu phẩy bằng hàm round
print("Diện tích trồng cây là:", round(S_con_lai, 2))


# Bài 3 Nhập ký tự c từ bàn phím
c = input("Nhập vào một kí tự c: ")

# Lệnh c.isupper() dùng để kiểm tra xem có phải CHỮ HOA không
if c.isupper():
    # Nếu đúng là chữ hoa thì biến nó thành chữ thường bằng c.lower()
    print("Kí tự sau khi đổi là:", c.lower())
else:
    # Nếu sai (là chữ thường) thì biến nó thành chữ hoa bằng c.upper()
    print("Kí tự sau khi đổi là:", c.upper())


# Bài 4 Nhập ký tự từ bàn phím
c = input("Nhập vào một kí tự c: ")

# Lệnh c.isalpha() dùng để kiểm tra xem c có phải chữ cái không
if c.isalpha():
    # Nếu đúng là chữ cái (hoa hoặc thường)
    print(c, "là kí tu alphabet")
else:
    # Nếu là số hoặc ký tự đặc biệt (@, #, $, ...)
    print(c, "không phải là kí tự alphabet")


# Để tính căn bậc hai, chúng ta cần dùng thêm thư viện math cơ bản của Python
import math

# Nhập 3 số từ bàn phím và đổi thành số thập phân (float)
a_chu = input("Nhập cạnh a: ")
b_chu = input("Nhập cạnh b: ")
c_chu = input("Nhập cạnh c: ")

a = float(a_chu)
b = float(b_chu)
c = float(c_chu)

# Bài 6 Kiểm tra điều kiện tam giác: Tổng 2 cạnh bất kỳ phải luôn lớn hơn cạnh còn lại
if (a + b > c) and (a + c > b) and (b + c > a):
    # Bước 1: Tính nửa chu vi p
    p = (a + b + c) / 2
    
    # Bước 2: Tính diện tích bằng công thức Heron (dùng math.sqrt để tính căn bậc hai)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    # Bước 3: In ra màn hình và làm tròn 1 chữ số thập phân bằng hàm round(S, 1)
    print("Diện tích của tam giác là:", round(S, 1))
else:
    # Nếu không thỏa mãn điều kiện ba cạnh tam giác
    print("Khong phai 3 canh cua tam giac")



