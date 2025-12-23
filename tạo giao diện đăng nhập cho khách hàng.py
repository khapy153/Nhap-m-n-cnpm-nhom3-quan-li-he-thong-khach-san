import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def login():
    print("=== ĐĂNG NHẬP KHÁCH HÀNG ===")

    email = input("Nhập email: ")
    password = input("Nhập mật khẩu: ")

    if not validate_email(email):
        print("❌ Email không đúng định dạng")
        return

    if password.strip() == "":
        print("❌ Mật khẩu không được để trống")
        return

    # Dữ liệu mẫu (giả lập database)
    db_email = "customer@gmail.com"
    db_password = "123456"

    if email == db_email and password == db_password:
        print("✅ Đăng nhập thành công")
    else:
        print("❌ Email hoặc mật khẩu không đúng")

login()
