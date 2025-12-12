import re

def validate_login(email: str, password: str):
    errors = {}

    # --- Kiểm tra email ---
    if not email:
        errors["email"] = "Email không được để trống."
    else:
        # Regex kiểm tra định dạng email
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, email):
            errors["email"] = "Email không đúng định dạng."

    # --- Kiểm tra mật khẩu ---
    if not password:
        errors["password"] = "Mật khẩu không được để trống."

    # Nếu có lỗi → trả về dict lỗi
    if errors:
        return False, errors

    # Không có lỗi → hợp lệ
    return True, "Dữ liệu hợp lệ."


# -----------------------------
# Ví dụ sử dụng
# -----------------------------
email_input = "test@gmail.com"
password_input = "123456"

is_valid, result = validate_login(email_input, password_input)

if is_valid:
    print("Đăng nhập hợp lệ:", result)
else:
    print("Lỗi nhập liệu:")
    for field, message in result.items():
        print(f"- {field}: {message}")
