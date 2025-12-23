import tkinter as tk
from tkinter import messagebox
import re

# ================== KIỂM TRA EMAIL ==================
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# ================== ĐĂNG NHẬP ==================
def login():
    email = entry_email.get()
    password = entry_password.get()

    if not validate_email(email):
        messagebox.showerror("Lỗi", "Email không hợp lệ")
        return

    if password.strip() == "":
        messagebox.showerror("Lỗi", "Mật khẩu không được để trống")
        return

    # Tài khoản mẫu (giả lập CSDL)
    if email == "customer@gmail.com" and password == "123456":
        messagebox.showinfo("Thành công", "Đăng nhập thành công")
        show_dashboard()
    else:
        messagebox.showerror("Thất bại", "Sai email hoặc mật khẩu")

# ================== HIỂN THỊ TRANG KHÁCH ==================
def show_dashboard():
    login_frame.pack_forget()
    dashboard_frame.pack()

# ================== ĐĂNG XUẤT ==================
def logout():
    dashboard_frame.pack_forget()
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    login_frame.pack()
    messagebox.showinfo("Thông báo", "Bạn đã đăng xuất")

# ================== CỬA SỔ CHÍNH ==================
root = tk.Tk()
root.title("Hệ thống khách hàng")
root.geometry("400x250")
root.resizable(False, False)

# ================== FRAME ĐĂNG NHẬP ==================
login_frame = tk.Frame(root)

tk.Label(login_frame, text="ĐĂNG NHẬP", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(login_frame, text="Email").pack()
entry_email = tk.Entry(login_frame, width=30)
entry_email.pack()

tk.Label(login_frame, text="Mật khẩu").pack(pady=5)
entry_password = tk.Entry(login_frame, width=30, show="*")
entry_password.pack()

tk.Button(login_frame, text="Đăng nhập", width=20, command=login).pack(pady=15)

login_frame.pack()

# ================== FRAME KHÁCH HÀNG (BẢO VỆ) ==================
dashboard_frame = tk.Frame(root)

tk.Label(dashboard_frame, text="TRANG KHÁCH HÀNG",
         font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(dashboard_frame,
         text="Bạn đang đăng nhập với quyền khách hàng").pack()

tk.Button(dashboard_frame, text="Đăng xuất",
          width=20, command=logout).pack(pady=20)

root.mainloop()
