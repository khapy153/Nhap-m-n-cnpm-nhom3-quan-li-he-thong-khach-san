# ================================
# ĐĂNG KÝ TÀI KHOẢN - PYTHON CONSOLE
# ================================

import re
import hashlib

# -------------------------------
# DATABASE GIẢ LẬP
# -------------------------------
users = []


# -------------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# -------------------------------
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# -------------------------------
def is_strong_password(password):
    if len(password) < 6:
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


# -------------------------------
def email_exists(email):
    for u in users:
        if u["email"] == email:
            return True
    return False


# -------------------------------
def register():
    print("\n=== ĐĂNG KÝ TÀI KHOẢN ===")

    name = input("Tên: ").strip()
    email = input("Email: ").strip()
    password = input("Mật khẩu: ").strip()

    # ---- VALIDATE ----
    if not name or not email or not password:
        print("❌ Không được để trống thông tin!")
        return

    if not is_valid_email(email):
        print("❌ Email không đúng định dạng!")
        return

    if email_exists(email):
        print("❌ Email đã tồn tại!")
        return

    if not is_strong_password(password):
        print("❌ Mật khẩu phải ≥ 6 ký tự và có ít nhất 1 số!")
        return

    # ---- TẠO TÀI KHOẢN ----
    users.append({
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": hash_password(password)
    })

    print("✅ Đăng ký thành công!")


# -------------------------------
def hien_thi_users():
    if not users:
        print("⚠ Chưa có tài khoản nào.")
        return

    print("\nDANH SÁCH USERS")
    for u in users:
        print(f"- {u['id']} | {u['name']} | {u['email']} | {u['password'][:10]}...")


# -------------------------------
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Đăng ký tài khoản")
        print("2. Xem danh sách users (test)")
        print("0. Thoát")

        ch = input("Chọn: ")

        if ch == "1":
            register()
        elif ch == "2":
            hien_thi_users()
        elif ch == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


# -------------------------------
menu()